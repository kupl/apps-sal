class Solution:
    def reorderedPowerOf2(self, N: int) -> bool:
        maxn = 10 ** 9
        twopower = 1
        twosets = set()
        while twopower <= maxn:
            twosets.add(twopower)
            twopower *= 2
        permutations = self.get_all_permutation(N)
        for p in permutations:
            if p[0] != '0' and int(p) in twosets:
                return True
        return False

    def get_all_permutation(self, num):
        perm = {''}
        for n in str(num):
            perm = {p[:i] + n + p[i:] for p in perm for i in range(len(p) + 1)}
        return perm

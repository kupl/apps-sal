class Solution:

    def reorderedPowerOf2(self, N: int) -> bool:

        def backtrack(idx, num):
            if idx == L:
                if num in two_set:
                    return True
                return False
            for v in counter:
                if idx == 0 and v == '0':
                    continue
                if counter[v] > 0:
                    counter[v] -= 1
                    if backtrack(idx + 1, num + v):
                        return True
                    counter[v] += 1
            return False
        perm_set = {N}
        ns = str(N)
        counter = Counter(ns)
        L = len(ns)
        two_set = set()
        num = 1
        while len(str(num)) <= L:
            if len(str(num)) == L:
                two_set.add(str(num))
            num *= 2
        return backtrack(0, '')

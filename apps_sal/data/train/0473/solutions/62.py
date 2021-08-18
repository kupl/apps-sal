class Solution:
    def countTriplets(self, a: List[int]) -> int:
        p = [a[0]]
        for i in range(1, len(a)):
            p.append(p[-1] ^ a[i])
        ans = 0
        for i in range(len(a) - 1):
            for j in range(i + 1, len(a)):
                v = p[j] ^ p[i] ^ a[i]
                for k in range(j, len(a)):
                    vv = p[k] ^ p[j]
                    if v == vv:
                        ans += 1
        return ans

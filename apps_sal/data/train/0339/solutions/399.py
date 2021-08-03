class Solution:
    def numTriplets(self, a1: List[int], a2: List[int]) -> int:
        m1 = Counter([x**2 for x in a1])
        m2 = Counter([x**2 for x in a2])
        ans = 0
        n1, n2 = len(a1), len(a2)
        for i in range(n1 - 1):
            for j in range(i + 1, n1):
                k = a1[i] * a1[j]
                if k in m2:
                    ans += m2[k]
        for i in range(n2 - 1):
            for j in range(i + 1, n2):
                k = a2[i] * a2[j]
                if k in m1:
                    ans += m1[k]
        return ans

class Solution:

    def numTriplets(self, a1: List[int], a2: List[int]) -> int:
        (ans, m1, m2, n1, n2) = (0, Counter([x ** 2 for x in a1]), Counter([x ** 2 for x in a2]), len(a1), len(a2))
        for i in range(n1 - 1):
            for j in range(i + 1, n1):
                ans += m2[a1[i] * a1[j]]
        for i in range(n2 - 1):
            for j in range(i + 1, n2):
                ans += m1[a2[i] * a2[j]]
        return ans

class Solution:
    def numFactoredBinaryTrees(self, A: List[int]) -> int:
        A.sort()
        O = {}
        ans = 0
        for a in A:
            if a not in O:
                O[a] = 1
            for k, v in list(O.items()):
                if a % k == 0 and a // k in O:
                    O[a] += v * O[a // k]
            ans += O[a]
        return ans % 1000000007

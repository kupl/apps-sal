class Solution:
    def numFactoredBinaryTrees(self, A: List[int]) -> int:
        A.sort()
        O = {}
        for a in A:
            if a not in O:
                O[a] = 1
            for k, v in list(O.items()):
                if a % k == 0 and a // k in O:
                    O[a] += v * O[a // k]
        return sum(O.values()) % 1000000007

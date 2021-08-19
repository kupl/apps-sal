class Solution:

    def countTriplets(self, A: List[int]) -> int:
        mp = {}
        for i in A:
            for j in A:
                k = i & j
                mp[k] = mp.get(k, 0) + 1
        result = 0
        for i in A:
            for j in mp:
                if i & j == 0:
                    result += mp[j]
        return result

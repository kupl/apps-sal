class Solution:
    def countTriplets(self, A: List[int]) -> int:
        memo = {}
        for i in A:
            for j in A:
                memo[i&j] = memo.get(i&j, 0)+1
        res = 0
        for num in A:
            for k in memo:
                if num&k==0:
                    res += memo[k]
        return res

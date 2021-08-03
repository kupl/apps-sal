class Solution:
    def numSubarraysWithSum(self, A: List[int], S: int) -> int:
        if not A or S < 0:
            return 0

        map = Counter()
        map[0] = 1
        sum = 0
        res = 0
        for num in A:
            sum += num
            if sum - S in map:
                res += map[sum - S]
            map[sum] += 1
        return res

class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        if not A or not K:
            return 0
        map = Counter()
        map[0] = 1
        sum = 0
        res = 0
        for num in A:
            sum += num
            sum %= K
            if sum < 0:
                sum += K
            if sum in map:
                res += map[sum]
            map[sum] += 1
        return res

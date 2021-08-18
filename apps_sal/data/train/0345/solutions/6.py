class Solution:
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        _sum = sum(nums)
        avg = _sum / m
        self.result = 10**10
        n = len(nums)
        cache = {}

        def recur(idx, m):
            if idx == n:
                return 0
            if m == 0:
                return 10**10
            if (idx, m) in cache:
                return cache[(idx, m)]
            _sum = 0
            result = 10**10
            i = idx
            while i < n:
                _sum += nums[i]
                if i == n - 1 or (_sum + nums[i + 1] > avg):
                    tmp = recur(i + 1, m - 1)
                    result = min(result, max(tmp, _sum))
                    if _sum > tmp:
                        cache[(idx, m)] = result
                        return result
                i += 1
            cache[(idx, m)] = result
            return result

        x = recur(0, m)
        return x

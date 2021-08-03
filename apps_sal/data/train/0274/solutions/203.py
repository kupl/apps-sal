class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        l = len(nums)
        if l == 1:
            if limit >= 0:
                return 1
            return 0
        max_count = i = 0
        j = 1

        def get_min():
            while min_list[0][1] < i:
                heappop(min_list)
            return min_list[0][1]

        def get_max():
            while max_list[0][1] < i:
                heappop(max_list)
            return max_list[0][1]

        min_list = []
        max_list = []

        heappush(min_list, (nums[0], 0))
        heappush(max_list, (-nums[0], 0))

        while l > j >= i:
            heappush(min_list, (nums[j], j))
            heappush(max_list, (-nums[j], j))
            mn = get_min()
            mx = get_max()
            diff = nums[mx] - nums[mn]
            if diff > limit:
                if j != i + 1:
                    max_count = max(max_count, j - i)
                    i = min(mn, mx) + 1
                else:
                    j += 1
                    i += 1
            else:
                j += 1
        if j == l and i < j - 1:
            max_count = max(max_count, j - i)
        return max_count

class Solution:

    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        """
        if not nums: return 0

        module = 10**9+7

        n = len(nums)
        heap = [[nums[i], i] for i in range(n)]
        heapq.heapify(heap)

        count = 0
        ans = 0

        while heap:    
            [val, idx] = heapq.heappop(heap)
            count += 1
            if count > right:
                break
            if count >= left:

                ans += val % module

            if idx+1 < n:
                heapq.heappush(heap, [val+nums[idx+1], idx+1])

        return ans % module

        """

        def subArraySum(target):
            count = 0
            (left, right) = (0, 0)
            running_sum = 0
            sub_sum = 0
            overall_sum = 0
            while right < n:
                running_sum += nums[right]
                sub_sum += nums[right] * (right - left + 1)
                while left <= right and running_sum > target:
                    sub_sum -= running_sum
                    running_sum -= nums[left]
                    left += 1
                count += right - left + 1
                overall_sum += sub_sum
                right += 1
            return (count, overall_sum % (10 ** 9 + 7))

        def findSum(target):
            if target == 0:
                return 0
            (l, r) = (min(nums) - 1, sum(nums) + 1)
            while l + 1 < r:
                m = l + (r - l) // 2
                (count, _) = subArraySum(m)
                if count < target:
                    l = m
                else:
                    r = m
            (count, summ) = subArraySum(r)
            return summ - r % (10 ** 9 + 7) * (count - target)
        return findSum(right) % (10 ** 9 + 7) - findSum(left - 1) % (10 ** 9 + 7)

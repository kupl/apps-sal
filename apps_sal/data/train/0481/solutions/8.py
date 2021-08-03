class Solution:
    def threeSumClosest(self, nums, target):
        res = 0
        nlen = len(nums)
        if nlen < 3:
            for num in nums:
                res += num
            return res

        lastdiff = sys.maxsize
        previous = None
        nums = sorted(nums)
        for idx in range(nlen - 2):
            num = nums[idx]
            if num == previous:
                continue
            i = idx + 1
            j = nlen - 1
            previous = num
            cur_sum = num

            while i < j:
                diff = 0
                cur_sum += (nums[i] + nums[j])
                if cur_sum == target:
                    return cur_sum
                if cur_sum < target:
                    diff = target - cur_sum
                    i += 1
                else:
                    diff = cur_sum - target
                    j -= 1
                if diff < lastdiff:
                    lastdiff = diff
                    res = cur_sum
                cur_sum = num

        return res

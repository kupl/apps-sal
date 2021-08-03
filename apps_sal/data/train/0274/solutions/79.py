class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        p1, p2, ans, cnt, min_, max_ = 0, 0, 0, {nums[0]: 1}, nums[0], nums[0]
        while True:
            if max_ - min_ <= limit:
                ans = max(ans, p2 - p1 + 1)
                if p2 == len(nums) - 1:
                    return ans
                p2 += 1
                if nums[p2] in cnt:
                    cnt[nums[p2]] += 1
                else:
                    cnt[nums[p2]] = 1
                max_ = max(max_, nums[p2])
                min_ = min(min_, nums[p2])
            else:
                num = nums[p1]
                p1 += 1
                if cnt[num] == 1:
                    del cnt[num]
                    if max_ == num:
                        max_ = max(cnt.keys())
                    if min_ == num:
                        min_ = min(cnt.keys())
                else:
                    cnt[num] -= 1

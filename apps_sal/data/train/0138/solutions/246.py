class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        nums.append(0)
        left = 0
        n = len(nums)
        first_neg = n
        last_neg = 0
        ct_neg = 0
        ans = 0
        for right in range(n):
            if nums[right] < 0:
                first_neg = min(first_neg, right)
                last_neg = max(last_neg, right)
                ct_neg += 1
            elif nums[right] == 0:
                if left < right:
                    if ct_neg & 1 == 0:
                        ans = max(ans, right - left)
                    else:
                        print(left, right, first_neg, last_neg)
                        ans = max(ans, right - first_neg - 1)
                        ans = max(ans, last_neg - left)
                left = right + 1
                first_neg = n
                last_neg = 0
                ct_neg = 0
        return ans

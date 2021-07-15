class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        result = 1
        start = 0
        end = start + result
        mini = float('inf')
        maxi = float('-inf')
        while end <= len(nums):
            #step 1, check if the min and max has changed?
            #In this step we disgarded the first element, and added the last element
            mini = min(nums[start:end])
            maxi = max(nums[start:end])
            if abs(mini - maxi) > limit:
                start += 1
                end += 1
            else:
                # step2, the current condition is satisfied, explore the next element until
                # the limit is broken
                end += 1
                while end <= len(nums):
                    mini = min(nums[end-1], mini)
                    maxi = max(nums[end-1], maxi)
                    if abs(mini - maxi) > limit:
                        result = max(result, end - start - 1)
                        start += 1
                        end = start + result
                        break
                    else:
                        end += 1
                        if end > len(nums):
                            result = max(result, end - start-1)
        return result


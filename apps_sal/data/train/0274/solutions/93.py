class Solution:

    def longestSubarray(self, nums: List[int], limit: int) -> int:
        answer = 1
        counts = {nums[0]: 1}
        subarray = deque([nums[0]])
        max_val = nums[0]
        min_val = nums[0]
        for i in range(1, len(nums)):
            counts[nums[i]] = counts.get(nums[i], 0) + 1
            max_val = max(max_val, nums[i])
            min_val = min(min_val, nums[i])
            subarray.append(nums[i])
            if abs(max_val - min_val) > limit:
                while subarray:
                    num = subarray.popleft()
                    counts[num] -= 1
                    if counts[num] == 0:
                        if max_val == num:
                            if subarray:
                                max_val = max(subarray)
                            else:
                                max_val = 0
                            break
                        elif min_val == num:
                            if subarray:
                                min_val = min(subarray)
                            else:
                                min_val = 10 ** 9 + 1
                            break
            answer = max(answer, len(subarray))
        return answer

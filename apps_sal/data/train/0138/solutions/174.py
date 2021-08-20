class Solution:

    def getMaxLen(self, nums: List[int]) -> int:
        max_len = 0
        start = -1
        is_pos = True
        for i in range(len(nums) + 1):
            if i == len(nums) or nums[i] == 0:
                if is_pos:
                    max_len = max(max_len, i - start - 1)
                else:
                    tmp = start + 1
                    while tmp < i:
                        if nums[tmp] < 0:
                            break
                        tmp += 1
                    max_len = max(max_len, i - tmp - 1)
                start = i
                is_pos = True
            else:
                if nums[i] < 0:
                    is_pos = not is_pos
                if is_pos:
                    max_len = max(max_len, i - start)
        return max_len

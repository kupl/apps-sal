class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        nums = []
        max_index = -1
        correct_blocks = 0
        latest_index = -1
        for _ in range(len(arr)):
            nums.append(0)
        for i in range(len(arr)):
            index = arr[i]-1
            
            if index == 0:
                try:
                    nums[index] = 1 + nums[index+1]
                    if nums[index+1] == m:
                        correct_blocks -= 1
                    if 1 + nums[index+1] == m:
                        correct_blocks += 1
                    if nums[index+1] != 0:
                        val = 1 + nums[index+1]
                        nums[index + nums[index+1]] = val
                        nums[index+1] = val
                except:
                    return 1
            elif index == len(arr)-1:
                try:
                    nums[index] = 1 + nums[index-1]
                    if nums[index-1] == m:
                        correct_blocks -= 1
                    if 1 + nums[index-1] == m:
                        correct_blocks += 1
                    if nums[index-1] != 0:
                        val = 1 + nums[index - 1]
                        nums[index - nums[index-1]] = val
                        nums[index-1] = val
                except:
                    return 1
            else:
                try:
                    val = 1 + nums[index-1] + nums[index+1]
                    if nums[index-1] == m:
                        correct_blocks -= 1
                    if nums[index+1] == m:
                        correct_blocks -= 1
                    if 1 + nums[index-1] + nums[index+1] == m:
                        correct_blocks += 1
                    nums[index] = val
                    if nums[index-1] != 0:
                        nums[index - nums[index-1]] = val
                        nums[index-1] = val
                    if nums[index+1] != 0:
                        nums[index + nums[index+1]] = val
                        nums[index+1] =va;
                except:
                    pass
            if correct_blocks > 0:
                latest_index = i+1
        return latest_index

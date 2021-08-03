# import numpy as np

class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        # locs = np.where(np.array(nums) == 1)[0]
        # return np.all(np.diff(locs) > k)
        # locs = [i for i in range(len(nums)) if  nums[i] == 1]
        # return all([locs[i+1] - locs[i] > k for i in range(len(locs)-1)])
        # for i in range(len(locs)-1):
        #     if locs[i+1] - locs[i] <= k:
        #         return False
        # return True

        last_loc, curr_loc = -1, -1
        for i, n in enumerate(nums):
            if n == 1:
                if last_loc == -1:
                    last_loc = i
                elif curr_loc == -1:
                    curr_loc = i
                curr_loc = i
                print((i, last_loc, curr_loc))
                if curr_loc - last_loc <= k and curr_loc != last_loc:
                    return False
                last_loc = i
        return True

class Solution:

    def kLengthApart(self, nums: List[int], k: int) -> bool:
        (last_loc, curr_loc) = (-1, -1)
        for (i, n) in enumerate(nums):
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

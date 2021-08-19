class Solution:

    def minOperations(self, nums: List[int]) -> int:
        nops = 0
        all_z = False
        while not all_z:
            all_z = True
            op2_mark = False
            for (idx, val) in enumerate(nums):
                if val != 0:
                    all_z = False
                else:
                    continue
                if val % 2 == 0:
                    if not op2_mark:
                        nops += 1
                        op2_mark = True
                    nums[idx] /= 2
                else:
                    nops += 1
                    if nums[idx] - 1 > 0:
                        if not op2_mark:
                            nops += 1
                            op2_mark = True
                    nums[idx] = (nums[idx] - 1) / 2
        return nops

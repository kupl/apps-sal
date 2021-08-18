class Solution:
    def minOperations(self, nums: List[int]) -> int:
        m = [bin(x)[2:].zfill(32) for x in nums]
        ret = 0
        for i in range(32):
            cnts = sum([1 if x[i] == '1' else 0 for x in m])
            ret += cnts
            if ret > 0:
                ret += 1
                pass
            pass
        return ret - 1

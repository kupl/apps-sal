class Solution:
    def minOperations(self, nums: List[int]) -> int:
        # make every element 1
        m = [bin(x)[2:].zfill(32) for x in nums]
        ret = 0
        # print(m)
        for i in range(32):
            # looking at the first digit. how many of you have it set to 1?
            cnts = sum([1 if x[i] == '1' else 0 for x in m])
            # print(\"%d: %d\" % (i, cnts))
            ret += cnts
            if ret > 0:
                ret += 1
                pass
            pass
        return ret - 1
        #first, remove

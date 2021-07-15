class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        pos = 0
        while pos<len(nums):
            #print(nums[pos:])
            try:
                pos = nums.index(1,pos)
                pos2 = nums.index(1,pos+1)
            except:
                break
            #print(pos,pos2)
            if pos2-pos-1<k:
                return False
            pos = pos2
        print(pos)
        return True

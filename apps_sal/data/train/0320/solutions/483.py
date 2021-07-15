class Solution:
    def minOperations(self, nums: List[int]) -> int:
        sumOp0,maxOp1=0,0
        for num in nums:
            op0,op1=list(bin(num)).count('1'),len(bin(num)[2:])-1
            sumOp0+=op0
            maxOp1=max(maxOp1,op1)
        return sumOp0+maxOp1

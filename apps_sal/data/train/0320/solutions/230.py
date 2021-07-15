class Solution:
    def minOperations(self, nums: List[int]) -> int:
        op=0
        a=[0]*len(nums)
        # print(a)
        # def modify(arr:List[int],op:int)-> None:
        while(nums!=a):
            # print(nums)
            for i in range(len(nums)):
                if nums[i]%2==0:
                    nums[i]=nums[i]//2
                else:
                    op+=1
                    nums[i]-=1
                    nums[i]=nums[i]//2
            op+=1
            # modify(nums,op)
        return (op-1)
            


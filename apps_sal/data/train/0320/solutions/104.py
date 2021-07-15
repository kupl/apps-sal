class Solution:
    def minOperations(self, nums: List[int]) -> int:
        def fun_call(num,mem):
            if not mem.get(num) is None:
                return mem[num]
            add=0
            mul=0
            old_num=num
            while(num>0):
                if num%2==0:
                    num//=2
                    mul+=1
                else:
                    num-=1
                    add+=1
            mem[old_num]=(add,mul)
            return mem[old_num]
        
        res=0
        mul_max=0
        mem={0:(0,0)}
        for i in range(len(nums)):
            add,mul=fun_call(nums[i],mem)
            res+=add
            mul_max=max(mul_max,mul)
        res+=mul_max
        return res
        


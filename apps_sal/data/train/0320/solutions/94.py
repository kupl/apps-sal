class Solution:
    def minOperations(self, nums: List[int]) -> int:
        
        def check(n):
            N_minus_one = 0
            N_div2 = 0
            while n>0:
                if n%2==0:
                    n = n//2
                    N_div2 += 1
                else:
                    n -= 1
                    N_minus_one += 1
            return N_minus_one,  N_div2
                
        
        N = len(nums)
        minus_one = []
        div2 = []
        for n in nums:
            N_minus_one, N_div2 = check(n)
            minus_one.append(N_minus_one)
            div2.append(N_div2)
            
        res = sum(minus_one)
        res += max(div2)
        print (minus_one)
        print (div2)
        return res
                


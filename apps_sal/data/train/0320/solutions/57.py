class Solution:
    def minOperations(self, nums: List[int]) -> int:
        
        div_arr,sub_arr=[],[]
        
        for n in nums:
            div=0
            sub=0
               
            while n:
                
                if n%2==1:
                    n-=1
                    sub+=1
                else:
                    n=n//2
                    div+=1
                    
            sub_arr.append(sub)
            div_arr.append(div)
            
            
        #print(sub_arr,div_arr)
        
        return max(div_arr) + sum(sub_arr) 


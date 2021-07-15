class Solution:
    def sumSubarrayMins(self, A: List[int]) -> int:
        
        res=[0]*(len(A)+1)
        A=[0]+A
        stack=[(0,0)]
        
        for i,num in enumerate(A):
            while stack and stack[-1][0]>num:
                stack.pop()
            j=stack[-1][1]
            res[i]=res[j]+(i-j)*num
            stack.append((num,i))
        return sum(res) % (10**9+7)


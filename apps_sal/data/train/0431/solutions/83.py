class Solution:
    def sumSubarrayMins(self, A: List[int]) -> int:
        left=[1]*len(A)
        right=[1]*len(A)
        stack=[]
        for i,v in enumerate(A):
            if i==0:
                stack.append(i)
                left[i]=1
            else:
                count=1
                while stack and A[stack[-1]] >v:
                    count+=left[stack.pop()]
                left[i]=count
                stack.append(i)
        stack=[]
        for i in range(len(A)-1,-1,-1):
            count=1
            while stack and A[stack[-1]]>=A[i]:
                count+=right[stack.pop()]
            right[i]=count
            stack.append(i)
       # print(left,right)
        sum=0
        for i in range(len(A)):
            sum=sum+(left[i]*right[i]*A[i])
        return sum%1000000007

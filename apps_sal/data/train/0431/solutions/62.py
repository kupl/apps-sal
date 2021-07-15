class Solution:
    def sumSubarrayMins(self, A: List[int]) -> int:
        ans=0
        
        
        st=[]
        n=len(A)
        left=[0]*n
        right=[0]*n
        mod=pow(10,9)+7
        for i in range(len(A)):
            c=1
            while st and st[-1][0]>A[i]:
                c+=st.pop()[1]
            
            left[i]=c
            st.append((A[i],c))
        
        
        st=[]
        for i in list(range(len(A)))[::-1]:
            c=1
            while st and st[-1][0]>=A[i]:
                c+=st.pop()[1]
            
            right[i]=c
            
            st.append((A[i],c))
        
        ans=0
        m=pow(10,9)+7
        
        print(left)
        print(right)
        for a,b,c in zip(A,left,right):
            ans+=a*b*c 
            ans=ans%m
                      
        return ans

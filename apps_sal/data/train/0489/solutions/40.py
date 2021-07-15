class Solution:
    def maxWidthRamp(self, x: List[int]) -> int:
        ma=0
        l=len(x)
        st=[(x[0],0)]
        for i in range(l):
            if x[i]<st[-1][0]:
                st.append((x[i],i))
        for i in range(l-1,-1,-1):
            while st!=[] and x[i]>=st[-1][0]:
                a,b= st.pop(-1)
                ma=max(i-b,ma)
            if st==[]:break
        return ma


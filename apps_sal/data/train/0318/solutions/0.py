class Solution:
    def maxSizeSlices(self, slices: List[int]) -> int:
        a,b,n=[slices[0]],[0],len(slices)
        for i in range(1,n):
            a.append(max(a[-1],slices[i]))
            b.append(max(b[-1],slices[i]))
        for i in range(2,2*n//3,2):
            aa,bb=[0]*(n-1),[0]*n
            for j in range(i,n-1): aa[j]=max(aa[j-1],a[j-2]+slices[j])
            for j in range(i+1,n): bb[j]=max(bb[j-1],b[j-2]+slices[j])
            a,b=aa,bb
        return max(a[-1],b[-1])

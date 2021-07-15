class Solution:
    def maxTurbulenceSize(self, A: List[int]) -> int:
        count=0
        vals=[]
        flag=0
        for i in range(2,len(A)):
            if A[i-2]<A[i-1]:
                flag=1
                if A[i-1]>A[i]:
                    if count==0: count+=2
                    count+=1
                else:
                    vals.append(count)
                    count=0
            elif A[i-2]>A[i-1]:
                flag=1
                if A[i-1]<A[i]:
                    if count==0: count+=2
                    count+=1
                else:
                    vals.append(count)
                    count=0
        vals.append(count)
        if flag:
            return max(max(vals),2)
        return max(max(vals),1)

class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        neg = []
        for i in range(len(arr)):
            if(arr[i]<0):
                neg.append(i)
        if(len(neg) == 0):
            return(sum(arr))
        if(len(neg) == len(arr) ):
            return max(arr)
        x1 = [0]*(len(neg))
        x2 = [0]*(len(neg))
        x1[0] = sum(arr[:neg[0]])
        x2[-1] = sum(arr[neg[-1]+1:])
        for j in range(1, len(neg)):
            for k in range(neg[j-1]+1, neg[j]):
                x1[j]+=arr[k]
            if(x1[j-1]+arr[neg[j-1]] > 0):
                x1[j]+=(x1[j-1]+arr[neg[j-1]])

        for j in range(len(neg)-2,-1,-1):
            for k in range(neg[j]+1,neg[j+1]):
                x2[j]+=arr[k]
            if(x2[j+1]+arr[neg[j+1]] > 0):
                x2[j]+=(x2[j+1]+arr[neg[j+1]])
        m = arr[0]
        for i in range(len(x1)):
            m = max(m, x1[i]+x2[i])
        return m

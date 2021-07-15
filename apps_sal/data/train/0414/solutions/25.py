class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        if(k>=len(arr)):
            return(max(arr))
        cons = 0
        ngr = [-1 for i in range(len(arr))]
        stack = [[arr[-1],len(arr)-1]]
        for i in range(len(arr)-2,-1,-1):
            while(len(stack)>0 and stack[-1][0]<arr[i]):
                stack.pop(-1)
            if(len(stack)!=0):
                ngr[i] = stack[-1][1]
            stack.append([arr[i],i])
        ngl = [-1 for i in range(len(arr))]
        stack = [[arr[0],0]]
        for i in range(1,len(arr),1):
            while(len(stack)>0 and stack[-1][0]<arr[i]):
                stack.pop(-1)
            if(len(stack)!=0):
                ngl[i] = stack[-1][1]
            stack.append([arr[i],i])
        marr = max(arr)
        for i in range(len(ngr)):
            if(ngr[i] == -1):
                if(arr[i] == marr):
                    return(marr)
                else:
                    if(ngl[i] + len(arr) - i>=k):
                        return(arr[i])
            else:
                if(i>0 and ngr[i]-i-1>=k-1):
                    return(arr[i])
                elif(i==0 and ngr[i]-i-1>=k):
                    return(arr[i])


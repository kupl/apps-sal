def binsearch(arr,x):
    if(arr[0]>x):
        return 0
    l=0
    h=len(arr)-1
    ret=-1
    while(l<=h):
        mid=(l+h)//2
        if(arr[mid]<=x):
            l=mid+1
        elif(arr[mid]>x):
            ret=mid
            h=mid-1
    return ret
class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        arr2.sort()
        m=len(arr2)
        n=len(arr1)
        dp={}
        # print(binsearch(arr2,0))
        def dfs(arr1,arr2,left,curr,dp):
            if(curr>=len(arr1)):
                return 0
            if((curr,left) in dp):
                return dp[(curr,left)]
            res1=sys.maxsize
            res2=0
            if(arr1[curr]>left):
                res1=dfs(arr1,arr2,arr1[curr],curr+1,dp)
            mid=binsearch(arr2,left)
            if(mid==-1):
                res2=sys.maxsize-1
            else:
                res2=dfs(arr1,arr2,arr2[mid],curr+1,dp)
            dp[(curr,left)]=min(res1,1+res2)
            return dp[(curr,left)]
        x=dfs(arr1,arr2,-sys.maxsize,0,dp)
        if(x>=(sys.maxsize-1)):
            return -1
        return x
            


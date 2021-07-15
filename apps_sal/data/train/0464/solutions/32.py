class Solution:
    def minOperations(self, n: int) -> int:
        arr=[]
        c=0
        for i in range(n):
            arr.append(2*i+1)
        tar1=len(arr)
        tar2=tar1
        if(tar1%2==0):
            tar2=tar2-1
        ans=arr.index(tar2)
        for i in range(ans):
            c+=tar1-arr[i]
        if(tar1!=tar2):
            c+=1
        return c

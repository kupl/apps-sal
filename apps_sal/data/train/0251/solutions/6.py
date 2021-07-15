class Solution:
    def clumsy(self, n: int) -> int:
        if n == 1:
            return 1
        arr = []
        temp = 0
        for i in range(n,0,-1):
            if temp == 0 or temp == 3:
                arr.append(i)
            elif temp == 1:
                arr[len(arr)-1] = arr[len(arr)-1]*i
            elif temp == 2:
                arr[len(arr)-1] = arr[len(arr)-1]//i
            temp = (temp+1)%4
        c = arr[0]
        for i in range(1,len(arr)):
            if i%2 == 1:
                c+=arr[i]
            else:
                c-=arr[i]
        return c

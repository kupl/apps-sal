class Solution:
    def minOperations(self, n: int) -> int:
        arr = [2*i+1 for i in range(n)]
        each = sum(arr)//n
    
        for i in range(n):
            arr[i] = each - arr[i]
        sums = 0
        for i in arr:
            if i>0:
                sums += i
        return sums
                

            


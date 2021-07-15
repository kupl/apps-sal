class Solution:
    def minOperations(self, n: int) -> int:
        
        total = 0
        arr = []
        
        for i in range(n):
            arr.append(2*i + 1)
        
        for i in range(int(len(arr)/2)):
            total += (arr[int(math.ceil(len(arr)/2 + i))] - arr[i]) / 2
        
        return int(total)
        
        


class Solution:
    def minOperations(self, n: int) -> int:
        arr = [2 * i + 1 for i in range(n)]
        
        target = sum(arr)//n
        ans = 0
        for i in range(len(arr)//2):
            ans += abs(arr[i] - target)
        return ans

class Solution:
    def minOperations(self, n: int) -> int:
        arr = [2 * i + 1 for i in range(n)]
        target = sum(arr)//n
        ans = 0
        for i in range(n//2):
            ans += abs(target - arr[i])
        return ans


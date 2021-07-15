class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        memo = {}
        def solve(i):
            if i in memo:
                return memo[i]
            
            ret = 1
            j = i-1
            while j>=max(0, i-d) and arr[j] < arr[i]:
                ret = max(ret, 1+solve(j))
                j -= 1
            j = i+1
            while j<=min(len(arr)-1, i+d) and arr[j]<arr[i]:
                ret = max(ret, 1+solve(j))
                j += 1
            memo[i] = ret
            return ret
        for i in range(len(arr)):
            solve(i)
        return max(memo.values())


class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        memo = [0] * len(arr)
        def jump(i):
            if memo[i]:
                return memo[i]
            ans = 1
            for di in [-1,1]:
                for x in range(1,d+1):
                    j = di *x +i
                    if 0 <= j <len(arr) and arr[j] < arr[i]:
                        ans = max(ans, jump(j)+1)
                    else:
                        break
            memo[i] = ans
            return memo[i]
        ans= 0
        for i in range(len(arr)):
            ans =max(ans, jump(i))
        return ans


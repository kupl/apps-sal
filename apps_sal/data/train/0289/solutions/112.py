class Solution:
    def maxSumTwoNoOverlap(self, A: List[int], L: int, M: int) -> int:
        def solve(arr, la, lb):
            n = len(arr)
            post = [0] * n
            pre = [0] * n
            ans = 0

            curr = 0
            for i in range(n-1, -1, -1):
                curr += arr[i]
                if i < n-lb:
                    curr -= arr[i+lb]
                    post[i] = max(curr, post[i+1]) 
                else:
                    post[i] = curr

            curr = 0
            for i in range(n):
                curr += arr[i]
                if i >= la:
                    curr -= arr[i-la]
                    pre[i] = max(curr, pre[i-1])
                else:
                    pre[i] = curr
                if i < n-1:
                    ans = max(ans, pre[i] + post[i+1])

            return ans
        
        return max(solve(A, L, M), solve(A, M, L))


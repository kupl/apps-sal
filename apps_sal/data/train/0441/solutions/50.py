class Solution:
    def consecutiveNumbersSum(self, N: int) -> int:
#         if N < 3: return 1
#         l = 1
#         r = 0
#         s = 0
#         ret = 0
#         while r < (N + 1) // 2:
#             r += 1
#             s += r
            
#             while s > N:
#                 s -= l
#                 l += 1
#             if s == N:
#                 ret += 1
#         return ret + 1
        ans = 0
        k = 1
        while True:
            a, b = divmod(N, 2 * k)
            if a >= k and b == k:
                ans += 1
            elif a < k:
                break
            a, b = divmod(N, 2 * k + 1)
            if a >= k + 1 and b == 0:
                ans += 1
            elif a < k + 1:
                break
            k += 1
        return ans + 1

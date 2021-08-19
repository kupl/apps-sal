# class Solution:
#     def minDays(self, n: int) -> int:
#         memo = {}
#         def helper(n):
#             # base case
#             if n<=1:
#                 return n
#             if n in memo:
#                 return memo[n]
#             minDays = float(\"inf\")
#             # don't need to check helper(n-1)
#             # if n is not divisible by 2, we eat 1 by 1 until it is divisible
#             # if n is not divisible by 3, we eat 1 by 1 until it is divisible
#             minDays = min(n%2 + helper(n//2), n%3 + helper(n//3)) + 1
#             memo[n] = minDays
#             return minDays

#         return helper(n)


class Solution:
    def minDays(self, n: int) -> int:
        ans = 0
        visited = set([n])
        q = collections.deque([n])
        while q:
            size = len(q)
            for _ in range(size):
                cur = q.popleft()
                if cur == 0:
                    return ans
                if cur - 1 not in visited:
                    visited.add(cur - 1)
                    q.append(cur - 1)
                if cur % 2 == 0 and cur // 2 not in visited:
                    visited.add(cur // 2)
                    q.append(cur // 2)
                if cur % 3 == 0 and cur // 3 not in visited:
                    visited.add(cur // 3)
                    q.append(cur // 3)
            ans += 1
        return -1

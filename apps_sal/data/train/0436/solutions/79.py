# from functools import lru_cache

# # 暴力bfs能过，但是是top-down的，比赛的时候我搞错了
# class Solution:
#     def minDays(self, n: int) -> int:

#         vis = set()
#         q = collections.deque([n])
#         cost = 1
#         while True:
#             for i in range(len(q)):
#                 cur = q.popleft()
#                 if cur <= 1:
#                     return cost
#                 if cur in vis:
#                     continue
#                 vis.add(cur)
#                 q.append(cur-1)
#                 if not cur % 2:
#                     q.append(cur//2)
#                 if not cur % 3:
#                     q.append(cur//3)
#             cost += 1

#         return dfs(n)

# 之后是剪枝

# 剪枝一，
class Solution:
    def minDays(self, n: int) -> int:
        ans = 1
        queue = [n]
        seen = set()
        while queue:  # bfs
            newq = []
            for x in queue:
                if x == 1:
                    return ans
                seen.add(x)
                if x - 1 not in seen:
                    newq.append(x - 1)
                if x % 2 == 0 and x // 2 not in seen:
                    newq.append(x // 2)
                if x % 3 == 0 and x // 3 not in seen:
                    newq.append(x // 3)
            ans += 1
            queue = newq


# 剪枝2 https://leetcode.com/problems/minimum-number-of-days-to-eat-n-oranges/discuss/794088/Intuitive-solution-with-Proof

# from functools import lru_cache
# class Solution:
#     def minDays(self, n: int) -> int:

#         @lru_cache(None)
#         def helper(n, one=0):
#             if one >= 3:
#                 return math.inf
#             if n < 1: return n

#             prev = helper(n - 1, one + 1)
#             if not n % 2:
#                 prev = min(prev, helper(n // 2))
#             if not n % 3:
#                 prev = min(prev, helper(n // 3))
#             return prev + 1

#         return helper(n)

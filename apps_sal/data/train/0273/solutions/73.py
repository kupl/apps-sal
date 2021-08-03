class Solution:
    def racecar(self, target):
        dp = [0, 1, 4] + [float('inf')] * target
        for t in range(3, target + 1):
            k = t.bit_length()
            if t == 2**k - 1:
                dp[t] = k
                continue
            for j in range(k - 1):
                dp[t] = min(dp[t], dp[t - 2**(k - 1) + 2**j] + k - 1 + j + 2)
            if 2**k - 1 - t < t:
                dp[t] = min(dp[t], dp[2**k - 1 - t] + k + 1)
        return dp[target]
# 比较难的一道题目，想了几天无果看了官方给的题解，还是很巧妙的。
# 用Ak表示k次连续的A，首先结尾一定不是R，开头的RAk可以放到最后。
# 那么最终指令应该形如Ak1RAk2R…RAkn。
# 容易得到奇数的ki与偶数的ki都是单调递减的，且各不相同。
# 并且到达或者超过目标位置之后继续执行A是没有意义的。
# 因此就有了DP的做法，如果下标位置是2k−1，那么可以直接Ak达到。
# 否则有两种情况，一是拐两次到达，正面一定有一次最大限度的2k−1，外加返回走j步（枚举j）。
# 二是直接走刚好超过2k−1，回走到终点。

#     def racecar(self, target: int) -> int:
#         # 0 -> 1 -> 3 -> 7 - > 15
#         # 1 -> 2 -> 4 -> 8 -> 16
#         # 从 0 出发，每次可以 R 或 A两个方向，选择。
#         # 可以记录每次到达的状态，
#         # BFS

#         d = deque([(0, 0, 1)])
#         visited = collections.defaultdict(set)
#         visited[0].add(1)
#         ans = float('inf')
#         flag = 0
#         while d:
#             flag += 1
#             # print(\"flag=\", flag,\", d=\", d)
#             l = len(d)
#             while l:
#                 l -= 1
#                 cur = d.popleft()
#                 # print(\"cur=\", cur)
#                 pos, cost, speed = cur
#                 if pos == target:
#                     ans = min(ans, cost)
#                     # continue
#                     return cost
#                 # use R
#                 cost += 1
#                 if 1:
#                     newspeed = -1 if speed > 0 else 1
#                     if not ((pos in visited and newspeed in visited[pos]) or (pos <= 0)):
#                         # print(\"past=\", cur,\", add=\", (pos, cost, -1))
#                         d.append(((pos, cost, newspeed)))
#                         visited[pos].add(newspeed)
#                         # 这里 if 里 break 不要瞎用，会跳出 while l 这个循环的。
#                 # use A
#                 if 1:
#                     if not (( speed in visited and (cost, speed * 2) in visited[pos]) or (pos + speed > target * 2) or (pos + speed <= 0)):

#                         # print(\"past=\", cur,\", add=\", (pos + speed, cost, speed * 2))
#                         d.append((pos + speed, cost, speed * 2))
#                         visited[pos].add(speed * 2)
#         return

#   # BFS 搞了半天，终于结束了。注意要剪枝。
# # 1. 首先 visited 加入的是 pos 和 speed。
# # 2. 第二是 位置不能超过 target * 2 。因为 如果超过了 target * 2那么要倒车，倒车从头开始，也要 走 target。这是 不合算的。
# # 3. 速度不能超过 2*target。  （可以不要）
# # 4. 不要 pos <0 的位置。
#         # pos    0 1 3 2 3
#         # speed  1 2 -1 1

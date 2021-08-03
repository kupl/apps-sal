from collections import deque


class Solution:
    def racecar(self, target):
        # 车子初始位置0，速度1
        # 遇到A，position += speed并且speed *= 2
        # 遇到R，speed = -1如果当前speed是1；speed = 1如果
        # 给定最终的位置target，问最短的sequence（由A和R组成）能够到达target
        if target == 0:
            return 0
        if target == 1:
            return 1
        if target == 2:
            return 4
        # 如果一直踩油门的话(连续3个A)
        # 则会到达0 -> 1 -> 3 -> 7
        #         k=1  k=2  k=3
        # dp[t]的定义是到达t位置最少需要走多少步
        dp = [2 ** 31 - 1] * (target + 1)
        dp[0], dp[1], dp[2] = 0, 1, 4
        for t in range(3, target + 1):
            k = t.bit_length()
            if t == 2 ** k - 1:
                # t = 7, 二进制111, k = 3
                # 此时表明踩3脚油门就能到了
                dp[t] = k
                continue

            # 此时必定 2 ** (k - 1) <= t <= 2 ** (k + 1)
            assert 2 ** (k - 1) <= t <= 2 ** (k + 1)

            # 情况1：走k - 1步，还没到t，回头再回头的策略
            # 然后用一个R和m个A去往回走
            # 这时候已经走了k - 1 + 1 + m + 1步（即A**(k - 1)RA**(m)R步)
            # 然后去dp里找剩余的步数t - 2 ** (k - 1) + 2 ** m
            for m in range(k - 1):
                # 注意：后面的k - 1 + m + 2是当前走了这么多步
                dp[t] = min(dp[t], dp[t - 2 ** (k - 1) + 2 ** m] + k - 1 + m + 2)

            # 情况2：直接k步，假设能够超过t，就采取再回头的策略
            # （已经走了k步, 就是在最后min函数括号里加的那一部分，加1是指一个R）
            # 然后再往回走
            # 走了k步距离就是2 ** k - 1，这个距离已经超越了t
            # 所以还要继续走2 ** k - 1 - t步才能走到t
            if 2 ** k - 1 - t > 0:
                dp[t] = min(dp[t], dp[2 ** k - 1 - t] + k + 1)
        return dp[target]

        # BFS解法，非最优，但是好想
#         queue = deque([(0, 1)])
#         # 状态是(location, speed)
#         visited = set([(0, 1)])

#         res = 0
#         while queue:
#             q_len = len(queue)
#             for _ in range(q_len):
#                 curr_pos, curr_speed = queue.popleft()
#                 if curr_pos == target:
#                     return res

#                 # case-1: 当前选择A
#                 new_pos = curr_pos + curr_speed
#                 new_speed = 2 * curr_speed
#                 if (new_pos, new_speed) not in visited:
#                     queue.append((new_pos, new_speed))
#                     visited.add((new_pos, new_speed))

#                 # case-2: 当前选择R
#                 new_pos = curr_pos
#                 new_speed = -1 if curr_speed > 0 else 1
#                 if (new_pos, new_speed) not in visited:
#                     queue.append((new_pos, new_speed))
#                     visited.add((new_pos, new_speed))
#             res += 1

#         return res

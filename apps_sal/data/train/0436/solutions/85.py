class Solution:
    def minDays(self, n):
        # 好题
        # 一共有n个橘子
        # 每天有3中选项吃橘子
        # 要么吃一个
        # 如果橘子数字可以被2整除，吃一半
        # 如果橘子数字可以被3整除，吃1 / 3
        # 问最少几天吃完

        # 思路：经典bfs，queue里放当前剩下的橘子数字即可
        queue = deque([n])
        visited = set()
        steps = 0
        
        # bfs中很经典的一个时间复杂度的优化就是利用visited数组
        while queue:
            q_len = len(queue)
            for _ in range(q_len):
                remain = queue.popleft()
                if remain == 0:
                    return steps
                if remain - 1 not in visited:
                    queue.append((remain - 1))
                    visited.add(remain - 1)
                if remain // 2 > 0 and remain % 2 == 0 and remain // 2 not in visited:
                    queue.append(remain // 2)
                    visited.add(remain // 2)
                if remain // 3 > 0 and remain % 3 == 0 and remain // 3 not in visited:
                    queue.append(remain // 3)
                    visited.add(remain // 3)
            steps += 1
        return steps

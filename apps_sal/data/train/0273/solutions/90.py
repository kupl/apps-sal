class Solution:
    def racecar(self, target: int) -> int:
        # 0 -> 1 -> 3 -> 7 - > 15
        # 1 -> 2 -> 4 -> 8 -> 16
        # 从 0 出发，每次可以 R 或 A两个方向，选择。
        # 可以记录每次到达的状态，
        # BFS

        d = deque([(0, 0, 1)])
        visited = collections.defaultdict(set)
        visited[0].add(1)
        ans = float('inf')
        flag = 0
        while d:
            flag += 1
            # print(\"flag=\", flag,\", d=\", d)
            l = len(d)
            while l:
                l -= 1
                cur = d.popleft()
                # print(\"cur=\", cur)
                pos, cost, speed = cur
                if pos == target:
                    ans = min(ans, cost)
                    # continue
                    return cost
                # use R
                cost += 1
                if 1:
                    newspeed = -1 if speed > 0 else 1
                    if not ((pos in visited and newspeed in visited[pos]) or (pos <= 0)):
                        # print(\"past=\", cur,\", add=\", (pos, cost, -1))
                        d.append(((pos, cost, newspeed)))
                        visited[pos].add(newspeed)
                        # 这里 if 里 break 不要瞎用，会跳出 while l 这个循环的。
                # use A
                if 1:
                    if not ((speed in visited and (cost, speed * 2) in visited[pos]) or (pos + speed > target * 2) or (pos + speed <= 0) or (speed > 2 * target)):

                        # print(\"past=\", cur,\", add=\", (pos + speed, cost, speed * 2))
                        d.append((pos + speed, cost, speed * 2))
                        visited[pos].add(speed * 2)
        return

        # pos    0 1 3 2 3
        # speed  1 2 -1 1

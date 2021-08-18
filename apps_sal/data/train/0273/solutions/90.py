class Solution:
    def racecar(self, target: int) -> int:

        d = deque([(0, 0, 1)])
        visited = collections.defaultdict(set)
        visited[0].add(1)
        ans = float('inf')
        flag = 0
        while d:
            flag += 1
            l = len(d)
            while l:
                l -= 1
                cur = d.popleft()
                pos, cost, speed = cur
                if pos == target:
                    ans = min(ans, cost)
                    return cost
                cost += 1
                if 1:
                    newspeed = -1 if speed > 0 else 1
                    if not ((pos in visited and newspeed in visited[pos]) or (pos <= 0)):
                        d.append(((pos, cost, newspeed)))
                        visited[pos].add(newspeed)
                if 1:
                    if not ((speed in visited and (cost, speed * 2) in visited[pos]) or (pos + speed > target * 2) or (pos + speed <= 0) or (speed > 2 * target)):

                        d.append((pos + speed, cost, speed * 2))
                        visited[pos].add(speed * 2)
        return

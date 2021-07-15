class Solution:
    def minDays(self, n):
        queue = deque([n])
        visited = set()
        visited.add(n)
        
        steps = 0
        
        while queue:
            q_len = len(queue)
            for _ in range(q_len):
                curr = queue.popleft()
                if curr == 0:
                    return steps
                if curr - 1 not in visited:
                    queue.append(curr - 1)
                    visited.add(curr - 1)
                if curr % 2 == 0 and curr // 2 > 0 and curr // 2 not in visited:
                    queue.append(curr // 2)
                    visited.add(curr // 2)
                if curr % 3 == 0 and curr // 3 > 0 and curr // 3 not in visited:
                    queue.append(curr // 3)
                    visited.add(curr // 3)
            steps += 1
        return -1

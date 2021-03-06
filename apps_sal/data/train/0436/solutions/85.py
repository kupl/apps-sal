class Solution:

    def minDays(self, n):
        queue = deque([n])
        visited = set()
        steps = 0
        while queue:
            q_len = len(queue)
            for _ in range(q_len):
                remain = queue.popleft()
                if remain == 0:
                    return steps
                if remain - 1 not in visited:
                    queue.append(remain - 1)
                    visited.add(remain - 1)
                if remain // 2 > 0 and remain % 2 == 0 and (remain // 2 not in visited):
                    queue.append(remain // 2)
                    visited.add(remain // 2)
                if remain // 3 > 0 and remain % 3 == 0 and (remain // 3 not in visited):
                    queue.append(remain // 3)
                    visited.add(remain // 3)
            steps += 1
        return steps

from collections import deque


class Solution:
    def kSimilarity(self, A: str, B: str) -> int:
        q = deque()
        q.append(A)
        visited = set([A])
        res = 0

        def neighbors(x):
            res = []
            i = 0
            while i < len(x) and x[i] == B[i]:
                i += 1
            for j in range(i + 1, len(A)):
                if x[j] == B[i]:
                    new_str = x[:i] + x[j] + x[i + 1:j] + x[i] + x[j + 1:]
                    if new_str not in visited:
                        visited.add(new_str)
                        res.append(new_str)
            return res

        while len(q) > 0:
            q_sz = len(q)
            for _ in range(q_sz):
                cur = q.popleft()
                if cur == B:
                    return res
                for neighbor in neighbors(cur):
                    q.append(neighbor)
            res += 1
        return res

from collections import deque


class Solution:
    def kSimilarity(self, A: str, B: str) -> int:

        length = len(A)
        q = deque([A])
        visited = set([A])
        step = 0
        while q:
            size = len(q)
            for _ in range(size):
                cur = q.popleft()

                if cur == B:
                    return step

                for i in range(length):
                    if cur[i] != B[i]:
                        break

                for j in range(i + 1, length):
                    if cur[j] != B[j] and cur[j] == B[i]:
                        new_str = cur[: i] + cur[j] + cur[i + 1: j] + cur[i] + cur[j + 1:]
                        if new_str not in visited:
                            q.append(new_str)
                            visited.add(new_str)

            step += 1

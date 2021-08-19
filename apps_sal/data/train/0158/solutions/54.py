from collections import deque


class Solution:
    def kSimilarity(self, A: str, B: str) -> int:
        # BFS
        # Key: at every step, we swap and make sure we put one char at correct pos, BFS makes sure it's shortest

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
                    # Key: NOT (cur[j] == B[i] or cur[i] == B[j])!!! Because in each BFS level we only need to make sure i pos can be corrected by swap(i,j), in the next level, since range of i and j is decreasing, width of BFS won't too large.
                    # But cur[i]==B[j] NOT guarantee i pos is corrected, next level it might still starts from i, thus range of search is width and got TLE
                    if cur[j] != B[j] and cur[j] == B[i]:
                        new_str = cur[: i] + cur[j] + cur[i + 1: j] + cur[i] + cur[j + 1:]
                        if new_str not in visited:
                            q.append(new_str)
                            visited.add(new_str)

            step += 1

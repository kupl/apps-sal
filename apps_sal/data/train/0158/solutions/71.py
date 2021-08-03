class Solution:
    def kSimilarity(self, A: str, B: str) -> int:
        if A == B:
            return 0

        queue = collections.deque([A])
        visited = set([A])
        step = 0

        while queue:
            for _ in range(len(queue)):
                curr = queue.popleft()
                for nxt in self.findNext(curr, B):
                    if nxt == B:
                        return step + 1
                    if nxt in visited:
                        continue
                    queue.append(nxt)
                    visited.add(nxt)
            step += 1
        return -1

    def findNext(self, curr, B):
        for i in range(len(curr)):
            if curr[i] != B[i]:
                break

        for j in range(i + 1, len(B)):
            if curr[j] == B[i]:
                yield curr[:i] + curr[j] + curr[i + 1: j] + curr[i] + curr[j + 1:]

class Solution:
    def kSimilarity(self, A: str, B: str) -> int:

        q = collections.deque()
        visited = set()
        q.append(A)
        visited.add(A)

        step = -1
        while q:
            step += 1
            lens = len(q)
            for _ in range(lens):
                curr = q.popleft()
                if curr == B:
                    return step
                for next in self._swap(curr, B):
                    if next in visited:
                        continue
                    q.append(next)
                    visited.add(next)

    def _swap(self, s, B):
        i = 0
        while s[i] == B[i]:
            i += 1
        for j in range(i + 1, len(s)):
            if s[j] == B[i]:
                yield s[:i] + s[j] + s[i + 1:j] + s[i] + s[j + 1:]

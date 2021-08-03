class Solution:
    def kSimilarity(self, A: str, B: str) -> int:
        def neighbor(s):
            i = 0
            while i < len(B) and s[i] == B[i]:
                i += 1
            for j in range(i + 1, len(B)):
                if s[j] == B[i]:
                    yield s[:i] + s[j] + s[i + 1:j] + s[i] + s[j + 1:]

        queue = deque([(A, 0)])
        visited = {A}
        while queue:
            s, d = queue.popleft()
            if s == B:
                return d
            for n in neighbor(s):
                if n not in visited:
                    visited.add(n)
                    queue.append([n, d + 1])

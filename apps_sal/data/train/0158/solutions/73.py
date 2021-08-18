class Solution:
    from collections import deque

    def kSimilarity(self, A: str, B: str) -> int:
        if A == B:
            return 0

        def G(pat):
            for i in range(len(B) - 1):
                if pat[i] != B[i]:
                    break

            ans = []
            for j in range(i + 1, len(B)):
                if pat[j] == B[i]:
                    ans.append(pat[:i] + pat[j] + pat[i + 1:j] + pat[i] + pat[j + 1:])
            return ans

        Q = deque([])
        visited = set()
        visited.add(A)
        Q.append((0, A))
        while(Q):
            lv, pat = Q.popleft()

            for new in G(pat):
                if new not in visited:
                    visited.add(new)
                    Q.append((lv + 1, new))
                    if new == B:
                        return lv + 1

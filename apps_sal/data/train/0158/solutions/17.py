from collections import deque


class Solution:
    def kSimilarity(self, A: str, B: str) -> int:
        def successor(s):
            i = 0
            while s[i] == B[i]:
                i += 1
            ans = []
            for j in range(i, len(s)):
                if s[j] == B[i]:
                    ans.append(s[:i] + s[j] + s[i + 1:j] + s[i] + s[j + 1:])
            return ans

        q = deque([(A, 0)])
        seen = set()
        while q:
            curr, dist = q.popleft()
            if curr == B:
                return dist
            if curr not in seen:
                seen.add(curr)
                q.extend([(suc, dist + 1) for suc in successor(curr)])

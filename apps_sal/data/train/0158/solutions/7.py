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
                for next in self._swap(curr, B):   # takes O(N)
                    if next in visited:
                        continue
                    q.append(next)
                    visited.add(next)

    def _swap(self, s, B):    # now only takes O(N)
        i = 0
        while s[i] == B[i]:   # if S[i]==B[i], we don't need to swap them - strong prune to makes sure swapped string always get more and more similar with B
            i += 1
        for j in range(i + 1, len(s)):
            if s[j] == B[i]:  # since B[i]!=s[i], if we swap s[j] to s[i], now B[i]=s[i]: this is how every swap make sure we get more and more closer to B
                yield s[:i] + s[j] + s[i + 1:j] + s[i] + s[j + 1:]

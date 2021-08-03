class Solution:
    def kSimilarity(self, A: str, B: str) -> int:
        '''
        A classic BFS solution to find the shortest path;
        The neighbors to each node string S are all the strings reachable with 1 swap, that match the first unmatched character in S.
        '''
        def getNeighbors(s):
            for i, c in enumerate(s):
                if c != B[i]:
                    break
            s = list(s)
            for j in range(i + 1, len(s)):
                if s[j] == B[i] and s[j] != B[j]:
                    s[i], s[j] = s[j], s[i]
                    yield(''.join(s))
                    s[j], s[i] = s[i], s[j]

        queue = collections.deque([A])
        seen = {A: 0}
        while queue:
            s = queue.popleft()
            if s == B:
                return seen[s]
            for n in getNeighbors(s):
                if n not in seen:
                    seen[n] = seen[s] + 1
                    queue.append(n)

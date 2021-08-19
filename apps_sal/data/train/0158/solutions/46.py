class Solution:

    def kSimilarity(self, A: str, B: str) -> int:
        if A == B:
            return 0

        def swap(S, i, j):
            a = list(S)
            (a[i], a[j]) = (a[j], a[i])
            return ''.join(a)
        n = len(A)
        steps = 0
        q = deque()
        visited = set()
        q.append(A)
        visited.add(A)
        while q:
            steps += 1
            sz = len(q)
            for _ in range(sz):
                S = q.popleft()
                i = 0
                while S[i] == B[i]:
                    i += 1
                for j in range(i + 1, n):
                    if S[j] != B[i] or S[j] == B[j]:
                        continue
                    T = swap(S, i, j)
                    if T == B:
                        return steps
                    if T not in visited:
                        q.append(T)
                        visited.add(T)
        return steps

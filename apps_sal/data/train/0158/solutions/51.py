class Solution:

    def kSimilarity(self, A: str, B: str) -> int:
        l = len(A)

        def neighbor(s, pos, target):
            visited = set()
            t = list(s)
            for i in range(pos + 1, l):
                if t[i] == target and (t[i], B[i]) not in visited:
                    visited.add((t[i], B[i]))
                    (t[pos], t[i]) = (t[i], t[pos])
                    yield ''.join(t)
                    (t[pos], t[i]) = (t[i], t[pos])
        step = 0
        index = 0
        seen = set()
        q = collections.deque()
        q.append((A, 0))
        seen.add(A)
        while q:
            lq = len(q)
            for j in range(lq):
                (tmp, k) = q.popleft()
                if tmp == B:
                    return step
                while k < l and tmp[k] == B[k]:
                    k += 1
                for n in neighbor(tmp, k, B[k]):
                    if n not in seen:
                        seen.add(n)
                        q.append((n, k))
            step += 1

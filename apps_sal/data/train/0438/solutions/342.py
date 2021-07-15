class Solution:
    def findLatestStep(self, A: List[int], T: int, last = -1) -> int:
        seen, ok = set(), set()
        A = [i - 1 for i in A]
        N = len(A)
        P = [i for i in range(N)]
        L = [1] * N
        def find(x):
            if x != P[x]:
                P[x] = find(P[x])
            return P[x]
        def union(a, b):
            a = find(a)
            b = find(b)
            P[b] = a
            L[a] += L[b]
            return L[a]
        step = 1
        for i in A:
            seen.add(i)
            if 0 < i and find(P[i - 1]) in ok: ok.remove(find(P[i - 1]))
            if i + 1 < N and find(P[i + 1]) in ok: ok.remove(find(P[i + 1]))
            if i - 1 in seen: L[i] = union(i, i - 1)
            if i + 1 in seen: L[i] = union(i, i + 1)
            if L[i] == T:
                ok.add(i)
            if len(ok):
                last = step
            step += 1
        return last

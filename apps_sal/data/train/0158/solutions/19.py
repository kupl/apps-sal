
class Solution:

    def kSimilarity(self, A: str, B: str) -> int:

        def neighbors(A):
            i = 0
            while A[i] == B[i]:
                i += 1

            for j in range(i + 1, len(B)):
                if A[i] != A[j] and A[j] == B[i]:
                    yield A[:i] + A[j] + A[i + 1:j] + A[i] + A[j + 1:]

        queue = [(A, 0)]
        seen = set([A])
        for s, val in queue:
            if s == B:
                return val

            for nxt_s in neighbors(s):
                if nxt_s not in seen:
                    queue.append((nxt_s, val + 1))
                    seen.add(nxt_s)
        return -1

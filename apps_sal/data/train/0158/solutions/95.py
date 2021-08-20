class Solution:

    def kSimilarity(self, A: str, B: str) -> int:

        def getSwap(S):
            for (i, c) in enumerate(S):
                if c != B[i]:
                    break
            T = list(S)
            for j in range(i + 1, len(S)):
                if S[j] == B[i]:
                    (T[i], T[j]) = (T[j], T[i])
                    yield ''.join(T)
                    (T[j], T[i]) = (T[i], T[j])
        (queue, cnt) = ([A], {A: 0})
        while queue:
            S = queue[0]
            del queue[0]
            if S == B:
                return cnt[S]
            for T in getSwap(S):
                if T not in cnt:
                    cnt[T] = cnt[S] + 1
                    queue.append(T)

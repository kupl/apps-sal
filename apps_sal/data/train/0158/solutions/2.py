class Solution:
    def kSimilarity(self, A: str, B: str) -> int:
        lsta, lstb = '', ''
        for i in range(len(A)):
            if A[i] != B[i]:
                lsta += A[i]
                lstb += B[i]
        q = [(0, lsta, lstb)]
        while q:
            time, la, lb = q.pop(0)
            if not lb:
                return time
            goal = lb[0]
            work, ls = None, []
            for i in range(1, len(la)):
                if la[i] == goal and la[0] == lb[i]:
                    work = True
                    break
            if work:
                q.append((time + 1, la[1:i] + la[i + 1:], lb[1:i] + lb[i + 1:]))
            else:
                for i in range(1, len(la)):
                    if la[i] == goal:
                        q.append((time + 1, la[1:i] + la[0] + la[i + 1:], lb[1:]))

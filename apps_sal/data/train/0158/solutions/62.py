class Solution:

    def kSimilarity(self, A: str, B: str) -> int:
        (lsta, lstb) = ([], [])
        for i in range(len(A)):
            if A[i] != B[i]:
                lsta.append(A[i])
                lstb.append(B[i])
        (A, B) = (''.join(lsta), ''.join(lstb))
        q = deque([(0, A, B)])
        while q:
            (cost, curr, goal) = q.popleft()
            if not curr:
                return cost
            need = goal[0]
            work = None
            for i in range(len(curr)):
                if curr[i] == goal[0] and goal[i] == curr[0]:
                    work = i
                    break
            if work:
                q.append((cost + 1, curr[1:work] + curr[work + 1:], goal[1:work] + goal[work + 1:]))
            else:
                for i in range(1, len(curr)):
                    if curr[i] == need:
                        q.append((cost + 1, curr[1:i] + curr[0] + curr[i + 1:], goal[1:]))

class Solution:
    def unhappyFriends(self, n: int, P: List[List[int]], A: List[List[int]]) -> int:
        unhappy = set()
        for i in range(n // 2):
            for j in range(i + 1, n // 2):
                Ai0, Ai1, Aj0, Aj1 = A[i][0], A[i][1], A[j][0], A[j][1]
                if P[Ai0].index(Ai1) > P[Ai0].index(Aj0) and P[Aj0].index(Aj1) > P[Aj0].index(Ai0):
                    unhappy.add(Ai0)
                    unhappy.add(Aj0)

                Ai0, Ai1, Aj0, Aj1 = A[i][1], A[i][0], A[j][0], A[j][1]
                if P[Ai0].index(Ai1) > P[Ai0].index(Aj0) and P[Aj0].index(Aj1) > P[Aj0].index(Ai0):
                    unhappy.add(Ai0)
                    unhappy.add(Aj0)

                Ai0, Ai1, Aj0, Aj1 = A[i][0], A[i][1], A[j][1], A[j][0]
                if P[Ai0].index(Ai1) > P[Ai0].index(Aj0) and P[Aj0].index(Aj1) > P[Aj0].index(Ai0):
                    unhappy.add(Ai0)
                    unhappy.add(Aj0)

                Ai0, Ai1, Aj0, Aj1 = A[i][1], A[i][0], A[j][1], A[j][0]
                if P[Ai0].index(Ai1) > P[Ai0].index(Aj0) and P[Aj0].index(Aj1) > P[Aj0].index(Ai0):
                    unhappy.add(Ai0)
                    unhappy.add(Aj0)

        return len(unhappy)

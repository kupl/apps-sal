class Solution:

    def canReorderDoubled(self, A: List[int]) -> bool:
        A.sort()
        N = len(A)
        count = collections.Counter(A)
        for i in range(N):
            if A[i] == 0 or A[i] not in count:
                continue
            elif A[i] < 0:
                if A[i] % 2 == 1 or count[A[i] / 2] == 0:
                    return False
                else:
                    count[A[i] / 2] -= count[A[i]]
                    if count[A[i] / 2] == 0:
                        del count[A[i] / 2]
                    del count[A[i]]
            elif count[A[i] * 2] == 0:
                return False
            else:
                count[A[i] * 2] -= count[A[i]]
                if count[A[i] * 2] == 0:
                    del count[A[i] * 2]
                del count[A[i]]
        return True

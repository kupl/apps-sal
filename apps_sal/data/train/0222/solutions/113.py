class Solution:
    def lenLongestFibSubseq(self, A: List[int]) -> int:
        d = {}
        for i, v in enumerate(A):
            d[v] = i

        l = len(A)

        res = -1
        for i in range(0, l):

            for j in range(i + 1, l):

                one_behind = A[j]
                two_behind = A[i]
                total = one_behind + two_behind

                c = 0
                while total in d:
                    if c == 0:
                        c += 3
                    else:
                        c += 1
                    tmp = one_behind
                    one_behind = total
                    two_behind = tmp
                    total = one_behind + two_behind

                res = max(res, c)

        return res

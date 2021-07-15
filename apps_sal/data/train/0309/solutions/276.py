class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        if len(A) < 3:
            return len(A)
        res = 2
        d = {k:{} for k in set(A)}
        for j in range(len(A)):
            zero = d[A[j]].get(0, 0) + 1
            res = max(res, zero)
            for step, l in list(d[A[j]].items()):
                d.setdefault(A[j] + step, {})
                prev = d[A[j] + step].get(step, 0)
                d[A[j] + step][step] = max(prev, l + 1)
                res = max(res, l + 1)
            for i in range(j):
                d.setdefault(2 * A[j] - A[i], {})
                d[2 * A[j] - A[i]].setdefault(A[j] - A[i], 2)
                # print(i, j, d[2 * A[j] - A[i]])
            d[A[j]] = {0: zero}
            # print(d)
        # res = max([max(v.values()) for v in d.values()])
        return res


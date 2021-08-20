class Solution:

    def lenLongestFibSubseq(self, A: List[int]) -> int:

        def memo(f):
            dic = {}

            def fa(*a):
                if a not in dic:
                    dic[a] = f(*a)
                return dic[a]
            return fa
        cache = {val: idx for (idx, val) in enumerate(A)}

        @memo
        def leng(i, j):
            if A[i] + A[j] not in cache:
                return 2
            return 1 + leng(j, cache[A[i] + A[j]])
        rec = 0
        for j in range(len(A)):
            for i in range(j):
                rec = max(rec, leng(i, j))
        return rec if rec > 2 else 0

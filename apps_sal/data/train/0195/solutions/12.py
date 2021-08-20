class Solution:

    def countTriplets(self, A: List[int]) -> int:
        l = len(A)
        Memo = {}
        for i in range(l):
            for j in range(i + 1):
                t = A[i] & A[j]
                if t not in Memo:
                    Memo[t] = 0
                if i == j:
                    Memo[t] += 1
                else:
                    Memo[t] += 2
        r = 0
        for a in A:
            for key in Memo:
                if key & a == 0:
                    r += Memo[key]
        return r

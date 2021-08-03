class Solution:
    def countTriplets(self, A: List[int]) -> int:

        N = len(A)
        ans = 0
        count = dict()

        for i in range(N):
            for j in range(N):
                tmp = A[i] & A[j]
                if tmp not in count:
                    count[tmp] = 1
                else:
                    count[tmp] += 1

        for k in range(N):
            for v in count:
                if A[k] & v == 0:
                    ans += count[v]
        return ans

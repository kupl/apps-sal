class Solution:

    def countTriplets(self, A: List[int]) -> int:
        d = dict()
        for i in range(len(A)):
            for j in range(len(A)):
                product = A[i] & A[j]
                if product in d:
                    d[product] += 1
                else:
                    d[product] = 1
        ans = 0
        for i in range(len(A)):
            for (k, v) in d.items():
                if A[i] & k == 0:
                    ans += v
        return ans

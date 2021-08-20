class Solution:

    def countTriplets(self, A: List[int]) -> int:
        n = len(A)
        cnt = collections.Counter()
        result = 0
        for i in A:
            for j in A:
                cnt[i & j] += 1
        for i in A:
            for (j, k) in cnt.items():
                if i & j == 0:
                    result += k
        return result

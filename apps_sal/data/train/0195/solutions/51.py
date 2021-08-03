from collections import defaultdict


class Solution:
    def countTriplets(self, A: List[int]) -> int:
        n = len(A)
        ans = 0
        counts = defaultdict(lambda: 0)
        for i in range(n):
            for j in range(n):
                counts[A[i] & A[j]] += 1

        for k in range(n):
            for num, count in list(counts.items()):
                if num & A[k] == 0:
                    ans += count
        return ans

#         (a & b) & c== 0

# # 0010
# # 0001
# # 1101
# # 0011
# # 1110

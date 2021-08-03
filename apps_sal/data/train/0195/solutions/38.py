from collections import defaultdict


class Solution:
    def countTriplets(self, A: List[int]) -> int:
        n = len(A)
        ans = 0
        A_counts = defaultdict(lambda: 0)
        for num in A:
            A_counts[num] += 1

        counts = defaultdict(lambda: 0)
        for n1, count1 in list(A_counts.items()):
            for n2, count2 in list(A_counts.items()):
                counts[n1 & n2] += count1 * count2

        for n1, count1 in list(A_counts.items()):
            for n2, count2 in list(counts.items()):
                if n1 & n2 == 0:
                    ans += count1 * count2
        return ans

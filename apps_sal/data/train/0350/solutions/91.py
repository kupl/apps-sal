import collections


class Solution:

    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
        counter = collections.defaultdict(int)
        result = 0
        start = startK = 0
        for (high, num) in enumerate(A):
            counter[num] += 1
            if len(counter) == K + 1:
                del counter[A[startK]]
                startK += 1
                start = startK
            if len(counter) == K:
                while counter[A[startK]] > 1:
                    counter[A[startK]] -= 1
                    startK += 1
                result += startK - start + 1
        return result

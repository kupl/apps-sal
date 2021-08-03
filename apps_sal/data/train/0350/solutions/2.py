from collections import OrderedDict


class Solution:
    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
        counter = OrderedDict()

        count = 0
        j = 0
        for i, n in enumerate(A):
            counter[n] = i
            counter.move_to_end(n)

            while len(counter) > K:
                j = counter.popitem(last=False)[1] + 1

            if len(counter) == K:
                count += next(iter(counter.values())) - j + 1

        return count

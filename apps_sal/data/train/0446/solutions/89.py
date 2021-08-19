from collections import Counter


class Solution:

    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        counter = collections.Counter(arr)
        for (i, j) in reversed(counter.most_common()):
            if k:
                if k - j >= 0:
                    del counter[i]
                    k -= j
                else:
                    break
        return len(counter)

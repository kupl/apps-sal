from collections import Counter


class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        m = Counter(arr)

        for x, y in sorted(list(m.items()), key=lambda x: x[1]):
            if k < 1:
                break

            a = max(y - k, 0)
            if a == 0:
                m.pop(x)
            k = max(k - y, 0)

        return len(m)

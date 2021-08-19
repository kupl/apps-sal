from collections import OrderedDict


class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        # im going to use a map, and we need to sort the map based on
        m = {}
        for i in arr:
            m[i] = m.get(i, 0) + 1

        for x, y in sorted(list(m.items()), key=lambda x: x[1]):
            if k < 1:
                break

            a = max(y - k, 0)
            if a == 0:
                m.pop(x)
            k = max(k - y, 0)

        return len(m)

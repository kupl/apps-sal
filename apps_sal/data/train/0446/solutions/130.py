from collections import Counter


class Solution:

    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        l = k
        if k == 0:
            l = -len(arr)
        L = [item for (items, c) in Counter(arr).most_common() for item in [items] * c][:-l]
        print(L)
        return len(set(L))

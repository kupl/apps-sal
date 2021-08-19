import collections


class Solution:

    def minSetSize(self, arr: List[int]) -> int:
        count = sorted(list(collections.Counter(arr).values()), reverse=True)
        toRemove = 0
        size = 0
        for c in count:
            toRemove += c
            size += 1
            if toRemove >= len(arr) / 2:
                break
        return size

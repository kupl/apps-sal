import collections


class Solution:

    def minSetSize(self, arr: List[int]) -> int:
        minSizeToRemove = len(arr) // 2
        counter = collections.Counter(arr)
        sortedCounters = sorted(counter.items(), key=lambda x: x[1], reverse=True)
        sum = 0
        minSet = set()
        for i in sortedCounters:
            sum += i[1]
            minSet.add(i[0])
            if sum >= minSizeToRemove:
                break
        return len(minSet)

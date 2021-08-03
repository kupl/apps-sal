import collections


class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        minSizeToRemove = len(arr) // 2
        # print(minSizeToRemove)
        counter = collections.Counter(arr)
        # print(counter)
        sortedCounters = sorted(counter.items(), key=lambda x: x[1], reverse=True)
        sum = 0
        minSet = set()
        for i in sortedCounters:

            sum += i[1]
            minSet.add(i[0])
            # print(i[0], i[1], sum, minSet)
            if sum >= minSizeToRemove:
                break

        return len(minSet)

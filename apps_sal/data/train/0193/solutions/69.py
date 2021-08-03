from collections import defaultdict


class Solution:
    def minSetSize(self, arr: List[int]) -> int:

        occurances = defaultdict(int)

        for num in arr:
            occurances[num] += 1

        dictlist = []
        for key, value in occurances.items():
            temp = [key, value]
            dictlist.append(temp)

        dictlist = sorted(dictlist, key=lambda x: x[1])

        count = 0
        removals = 0
        while (count < len(arr) / 2):
            count += dictlist[-1][1]
            dictlist.pop()
            removals += 1

        return removals

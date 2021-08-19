class Solution:

    def minSetSize(self, arr) -> int:
        counter = {}
        for val in arr:
            if val not in counter:
                counter[val] = 0
            counter[val] += 1
        values = []
        for val in counter:
            values.append(counter[val])
        values.sort(reverse=True)
        total = 0
        nhalf = len(arr) // 2
        new_n = len(arr)
        i = 0
        while new_n > nhalf:
            total += 1
            new_n -= values[i]
            i += 1
        return total

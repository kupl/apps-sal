class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        values = {}
        for i in range(len(arr)):
            val = 0
            for j in range(i, len(arr)):
                val ^= arr[j]
                if val not in values:
                    values[val] = {
                        'start': {},
                        'end': {}
                    }
                if i not in values[val]['start']:
                    values[val]['start'][i] = 0
                values[val]['start'][i] += 1
                if j not in values[val]['end']:
                    values[val]['end'][j] = 0
                values[val]['end'][j] += 1

        total = 0

        for val in values:
            for index in values[val]['end']:
                if index + 1 in values[val]['start']:
                    total += values[val]['start'][index + 1] * values[val]['end'][index]

        return total

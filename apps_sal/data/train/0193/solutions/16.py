class Solution:

    def minSetSize(self, arr: List[int]) -> int:
        half = len(arr) / 2
        counts = {}
        for val in arr:
            if val in counts.keys():
                counts[val] += 1
            else:
                counts[val] = 1
        count = 0
        included = 0
        for key in sorted(counts, key=counts.get, reverse=True):
            count += counts[key]
            included += 1
            if count >= half:
                return included

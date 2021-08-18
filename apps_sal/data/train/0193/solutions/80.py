class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        length = len(arr)
        counts = {}
        for num in arr:
            if num not in counts:
                counts[num] = 1
            else:
                counts[num] += 1

        descending = sorted(counts.values(), reverse=True)
        count = 0
        total = 0
        for num in descending:
            total += num
            count += 1
            if total >= length / 2:
                return count

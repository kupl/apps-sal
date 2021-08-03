from collections import defaultdict


class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        counter = defaultdict(int)
        for a in arr:
            counter[a] += 1
        nums = list(counter.keys())
        nums.sort(key=lambda x: counter[x], reverse=True)
        count = 0
        total = 0
        half = (len(arr) + 1) // 2
        for n in nums:
            total += counter[n]
            count += 1
            if total >= half:
                return count

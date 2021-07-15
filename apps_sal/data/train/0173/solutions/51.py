from collections import defaultdict
class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        if len(arr) % 2 == 1:
            return False
        d = defaultdict(int)
        count = 0
        for i, num in enumerate(arr):
            key = k - (num % k)
            if key in d and d[key] >= 1:
                count += 1
                d[key] -= 1
            else:
                d[(num % k) or k] += 1
        return count == len(arr) // 2

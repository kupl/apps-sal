from collections import Counter

class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        
        n = len(arr)
        counts = Counter(arr)
        sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
        count = 0
        ans = 0
        for sc in sorted_counts:
            count += sc[1]
            ans += 1
            if count >= n//2:
                return ans
        return ans

from collections import Counter
class Solution:
    
    def minSetSize(self, arr: List[int]) -> int:
        counts = Counter(arr)
        elements = 0
        count = len(arr) / 2
        for (key, value_count) in sorted(list(counts.items()), key=lambda x: x[1], reverse=True):
            if count <= 0:
                break
            elements += 1
            count -= value_count
        return elements


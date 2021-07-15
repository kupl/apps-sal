class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        N = len(arr)
        count = collections.Counter()
        for n in arr:
            count[n] += 1
        
        sorted_count = sorted(list(count.keys()), key=lambda c: count[c], reverse=True)
        removed_count = 0
        res = 0
        for c in sorted_count:
            removed_count += count[c]
            res += 1
            if removed_count >= (N + 1) // 2:
                break
        return res


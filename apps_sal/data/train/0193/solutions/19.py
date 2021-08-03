class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        half = len(arr) // 2
        count = ans = 0
        counts = Counter(arr)

        for k, v in counts.most_common():
            ans += v
            count += 1
            if ans >= half:
                return count

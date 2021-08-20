class Solution:

    def minSetSize(self, arr: List[int]) -> int:
        freqs = Counter(arr)
        sorted_freqs = sorted(list(freqs.items()), key=lambda x: x[1], reverse=True)
        print(sorted_freqs)
        half_len = len(arr) / 2
        current_len = 0
        res = 0
        for (i, j) in sorted_freqs:
            res += 1
            current_len += j
            if current_len >= half_len:
                return res

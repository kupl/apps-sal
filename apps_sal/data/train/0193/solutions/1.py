class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        freq = Counter(arr)
        final_length = 0
        half = len(arr) / 2
        reduce = 0
        for n, f in freq.most_common():
            final_length += f
            reduce += 1
            if final_length >= half:
                return reduce

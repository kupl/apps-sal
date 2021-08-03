class Solution:
    def minSetSize(self, arr: List[int]) -> int:

        d = {}
        n = len(arr)

        for a in arr:
            d[a] = d.get(a, 0) + 1

        val = sorted(list(d.items()), key=lambda x: x[1])[::-1]

        count = 0

        for i, (_, val_i) in enumerate(val):
            count += val_i

            if count >= n // 2:
                return i + 1

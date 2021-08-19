class Solution:

    def largestValsFromLabels(self, values: List[int], labels: List[int], num_wanted: int, use_limit: int) -> int:
        items = sorted(list(zip(values, labels)), key=lambda x: -x[0])
        res = 0
        freq = defaultdict(int)
        n = 0
        for (i, (val, label)) in enumerate(items):
            if freq[label] < use_limit:
                freq[label] += 1
                res += val
                n += 1
            if n == num_wanted:
                break
        return res

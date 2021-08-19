class Solution:

    def largestValsFromLabels(self, values: List[int], labels: List[int], num_wanted: int, use_limit: int) -> int:
        empty = {i: use_limit for i in set(labels)}
        ans = 0
        pairs = [(values[i], labels[i]) for i in range(len(values))]
        pairs.sort(key=lambda x: -x[0])
        for (index, pair) in enumerate(pairs):
            if empty[pair[1]] > 0 and num_wanted > 0:
                ans += pair[0]
                empty[pair[1]] -= 1
                num_wanted -= 1
        return ans

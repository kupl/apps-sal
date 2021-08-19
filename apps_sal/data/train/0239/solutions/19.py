class Solution:

    def largestValsFromLabels(self, values: List[int], labels: List[int], num_wanted: int, use_limit: int) -> int:
        counts = collections.defaultdict(int)
        vl = sorted(zip(values, labels))
        ans = 0
        while num_wanted and vl:
            (val, lab) = vl.pop()
            if counts[lab] < use_limit:
                ans += val
                counts[lab] += 1
                num_wanted -= 1
        return ans

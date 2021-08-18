class Solution:
    def largestValsFromLabels(self, values: List[int], labels: List[int], num_wanted: int, use_limit: int) -> int:

        l2v = collections.defaultdict(list)
        for v, l in zip(values, labels):
            l2v[l].append(v)
        pool = []
        for l in l2v:
            pool += sorted(l2v[l])[-use_limit:]
        return sum(sorted(pool)[-num_wanted:])

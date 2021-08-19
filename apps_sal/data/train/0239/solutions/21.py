class Solution:
    def largestValsFromLabels(self, values: List[int], labels: List[int], num_wanted: int, use_limit: int) -> int:
        vls = sorted(zip(values, labels), reverse=True)
        l2v = defaultdict(list)
        for v, l in vls:
            l2v[l].append(v)
        chosen = []
        l_use = defaultdict(int)
        for i, (v, l) in enumerate(vls):
            if l_use[l] < use_limit:
                chosen.append((v, l))
                l_use[l] += 1
                if len(chosen) >= num_wanted:
                    break
        # print(chosen)
        return sum(v for v, l in chosen)

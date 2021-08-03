class Solution:
    def get_result(self, sl, d):
        for k in sl:
            if d[k] == 0:
                continue
            if 2 * k not in d:
                return False
            v = d[k]
            v2 = d[2 * k]
            if v > v2:
                return False
            d[k] -= v
            d[2 * k] -= v
        return True

    def canReorderDoubled(self, A: List[int]) -> bool:
        d = dict()
        num_zeros = 0
        for a in A:
            if a == 0:
                num_zeros += 1
                continue
            if a in d:
                d[a] += 1
            else:
                d[a] = 1
        neg = [k for k in list(d.keys()) if k < 0]
        pos = [k for k in list(d.keys()) if k > 0]
        if num_zeros % 2 != 0:
            return False
        sorted_pos = sorted(pos)
        sorted_neg = sorted(neg, reverse=True)
        res = self.get_result(sorted_pos, d)
        if not res:
            return False
        res = self.get_result(sorted_neg, d)
        if not res:
            return False
        return sum(list(d.values())) == 0

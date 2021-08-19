class Solution:

    def threeSumMulti(self, A: List[int], target: int) -> int:
        d = Counter(A)
        keys = sorted(d.keys())
        count = 0
        for (i, a) in enumerate(keys):
            if a <= target // 3:
                for b in keys[i + 1:]:
                    if target - a - b <= b:
                        break
                    elif target - a - b in d:
                        count += d[a] * d[b] * d[target - a - b]
            else:
                break
        for k in keys:
            if target != 3 * k and target - 2 * k in d:
                count += math.comb(d[k], 2) * d[target - 2 * k]
        if 3 * (target // 3) == target:
            count += math.comb(d[target // 3], 3)
        return count % (10 ** 9 + 7)

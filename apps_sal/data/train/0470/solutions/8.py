import collections as clc
import itertools as it


class Solution:
    BASE = 10 ** 9 + 7

    def threeSumMulti(self, A: List[int], target: int) -> int:
        counter = clc.Counter(A)
        values = sorted(counter)
        n = len(values)
        pair_sums = clc.Counter()
        ans = 0
        for k in range(n):
            if 3 * values[k] == target and counter[values[k]] >= 3:
                cnt = counter[values[k]]
                ans = (ans + cnt * (cnt - 1) * (cnt - 2) // 6) % self.BASE
        for (j, k) in it.combinations(range(n), 2):
            if 2 * values[j] + values[k] == target and counter[values[j]] >= 2:
                cntj = counter[values[j]]
                cntk = counter[values[k]]
                ans = (ans + cntj * (cntj - 1) // 2 * cntk) % self.BASE
            if values[j] + 2 * values[k] == target and counter[values[k]] >= 2:
                cntj = counter[values[j]]
                cntk = counter[values[k]]
                ans = (ans + cntk * (cntk - 1) // 2 * cntj) % self.BASE
        for k in range(2, n):
            j = k - 1
            for i in range(j):
                pair_sums[values[i] + values[j]] += counter[values[i]] * counter[values[j]]
            ans = (ans + counter[values[k]] * pair_sums[target - values[k]]) % self.BASE
        return ans % self.BASE

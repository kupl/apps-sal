from collections import defaultdict
class Solution:
    def threeSumMulti(self, A: List[int], target: int) -> int:
        single = defaultdict(int)
        double = defaultdict(int)
        ans = 0
        for x in A:
            ans += double[target - x]
            for k, v in single.items():
                double[k + x] += v
            single[x] += 1
        return ans % (10**9 + 7)

class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        # start with smallest number
        if len(nums) % k != 0:
            return False

        d = collections.Counter(nums)
        s = list(d)
        s.sort()

        for n in s:
            if n in d:
                c = collections.Counter({m: d[n] for m in range(n, n + k)})
                if all([key in d and d[key] >= c[key] for key in c]):
                    d -= c
                else:
                    return False
        return True

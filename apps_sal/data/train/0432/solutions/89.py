class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        if k == 1:
            return True
        if len(nums) % k:
            return False
        d = defaultdict(int)

        for n in nums:
            d[n] += 1

        count = 0
        iters = len(nums) // k

        while iters > 0:
            prev = None
            count = 0
            iters -= 1
            for key in sorted(d):
                if count != 0 and not count % k:
                    break
                if not prev or (d[key] > 0 and prev + 1 == key):
                    d[key] -= 1
                    prev = key
                    count += 1
                else:
                    return False
            a = list(d.keys())
            for key in a:
                if d[key] == 0:
                    d.pop(key)
        if len(list(d.keys())):
            return False
        return True

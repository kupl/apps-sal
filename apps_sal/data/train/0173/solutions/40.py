class Solution:

    def canArrange(self, arr: List[int], k: int) -> bool:
        h = collections.defaultdict(int)
        invalid = 0
        for n in arr:
            mod = n % k
            completment = k - mod if mod > 0 else 0
            if h[completment] > 0:
                h[completment] -= 1
                if h[completment] == 0:
                    invalid -= 1
            else:
                h[mod] += 1
                if h[mod] == 1:
                    invalid += 1
        return invalid == 0

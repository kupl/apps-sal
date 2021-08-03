class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        h = collections.Counter(i % k for i in arr)
        if 0 in h:
            if h[0] % 2 != 0:
                return False
        for x in h:
            if x > 0 and h[x] != h[k - x]:
                return False
        return True

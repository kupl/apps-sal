class Solution:

    def canArrange(self, arr: List[int], k: int) -> bool:
        tmp = collections.Counter()
        for x in arr:
            tmp[x % k] += 1
        for (c, v) in list(tmp.items()):
            if c == 0 and v % 2 != 0:
                return False
            elif c != 0 and v != tmp[k - c]:
                return False
        return True

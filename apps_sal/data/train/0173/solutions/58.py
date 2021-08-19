class Solution:

    def canArrange(self, arr: List[int], k: int) -> bool:
        a = arr
        c = collections.Counter()
        for x in a:
            r = x % k
            t = k - r if r else r
            if t in c:
                c[t] -= 1
                if c[t] == 0:
                    del c[t]
            else:
                c[r] += 1
        return not c

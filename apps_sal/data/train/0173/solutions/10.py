class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        d = collections.Counter()
        for e in arr:
            t = e % k
            d[t] += 1
        key = d.keys()
        print(d)
        for e in key:
            if e == 0:
                continue
            if d[e] != d[k - e]:
                return False
            else:
                if e == k // 2 and k % 2 == 0 and d[e] % 2 != 0:
                    return False
        return True

class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        d = collections.Counter([i % k for i in arr])
        pair = 0
        # print(d)
        for i in list(d.keys()):
            if k - i == i:
                if i in d:
                    if d[i] > 1:
                        pair += d[i] // 2
                        d[i] = 0
                    else:
                        continue
            if k - i in d:
                t = min(d[i], d[k - i])
                pair += t
                d[i] -= t
                d[k - i] -= t
        # print(pair)
        # print(len(arr))
        # print(d.values())
        if 0 in d:
            pair += d[0] // 2
            d[0] = 0
        print(pair)
        if pair == len(arr) // 2:
            return 1
        return 0

class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        rangelist = [None] * (n + 1)

        for i in range(n + 1):
            s = max(i - ranges[i], 0)
            e = min(i + ranges[i], n)

            if rangelist[s] == None:
                rangelist[s] = (s, e)
            else:
                rangelist[s] = (s, max(rangelist[s][1], e))

        curr = mx = 0
        count = 0
        i = 0
        while i < len(rangelist):
            while True and i < len(rangelist):
                if(rangelist[i] == None):
                    i += 1
                    continue
                s, e = rangelist[i]
                if s > mx:
                    return -1
                if s > curr:
                    break
                mx = max(e, mx)
                i += 1
            if curr != mx:
                curr = mx
                count += 1

        if mx < n:
            return -1
        return count

INF = int(1e9)


class Solution:
    def shortest_subarrays(self, a, target):
        cum = [0]
        for x in a:
            cum.append(cum[-1] + x)
        hist = {0: 0}
        ret = [INF]
        for i in range(1, len(cum)):
            ci = cum[i]
            begin = hist.get(ci - target, -1)
            if begin >= 0:
                ret.append(min(i - begin, ret[-1]))
            else:
                ret.append(ret[-1])
            hist[ci] = i
        return ret

    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        forward = self.shortest_subarrays(arr, target)
        backward = self.shortest_subarrays(reversed(arr), target)

        ret = INF
        for i in range(1, len(arr) - 1 + 1):
            ret = min(ret, forward[i] + backward[len(arr) - i])
        if ret >= INF:
            return -1
        return ret

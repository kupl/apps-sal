from heapq import heappush, heappop
from collections import defaultdict


class Solution(object):

    def rankTeams(self, vs):
        sz = len(vs[0])
        cnt = defaultdict(lambda: [0] * (sz + 1))
        for v in vs:
            for (i, c) in enumerate(v):
                cnt[c][i] -= 1
                cnt[c][sz] = c
        az = list(cnt.keys())
        az.sort(key=lambda cc: cnt[cc])
        return ''.join(az)

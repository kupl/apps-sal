import collections


class Solution:

    def canReorderDoubled(self, A: List[int]) -> bool:
        neg = collections.Counter()
        pos = collections.Counter()
        for n in A:
            if n >= 0:
                pos[n] += 1
            else:
                neg[n] += 1
        for n in sorted(neg, reverse=True):
            if neg[n * 2] < neg[n]:
                return False
            neg[n * 2] -= neg[n]
            del neg[n]
            if neg[n * 2] == 0:
                del neg[n * 2]
        if len(neg) != 0:
            return False
        for n in sorted(pos):
            if pos[n * 2] < pos[n]:
                return False
            pos[n * 2] -= pos[n]
            del pos[n]
            if pos[n * 2] == 0:
                del pos[n * 2]
        if len(pos) != 0:
            return False
        return True

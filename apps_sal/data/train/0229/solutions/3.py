import collections


class Solution:
    def canReorderDoubled(self, A: List[int]) -> bool:
        ''' Place all values into dicts and start counting from the bottom
        '''
        if not A:
            return True

        pos = collections.defaultdict(int)
        neg = collections.defaultdict(int)
        zero = 0

        for v in A:
            if v > 0:
                pos[v] += 1
            if v < 0:
                neg[-v] += 1
            if v == 0:
                zero += 1

        b = self.check(pos)
        if not b:
            return False
        b = self.check(neg)
        if not b:
            return False

        return zero % 2 == 0

    def check(self, d):

        while d:
            v = min(d)
            if not 2 * v in d:
                return False
            if d[v] > d[2 * v]:
                return False

            elif d[v] == d[2 * v]:
                del d[v]
                del d[2 * v]
            else:
                d[2 * v] -= d[v]
                del d[v]
        return True

import collections


class Window:

    def __init__(self):
        self.num = 0
        self.dic = collections.Counter()

    def add(self, v: int) -> int:
        if self.dic[v] == 0:
            self.num += 1
        self.dic[v] += 1
        return self.num

    def remove(self, v: int) -> int:
        self.dic[v] -= 1
        if self.dic[v] == 0:
            self.num -= 1
        return self.num


class Solution:

    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
        wk = Window()
        wm = Window()
        sk = 0
        sm = 0
        e = 0
        ans = 0
        while e < len(A):
            ce = A[e]
            nk = wk.add(ce)
            nm = wm.add(ce)
            if nk < K:
                e += 1
            elif nk == K:
                while nm != K - 1:
                    nm = wm.remove(A[sm])
                    sm += 1
                ans += sm - sk
                e += 1
            else:
                while nk != K:
                    nk = wk.remove(A[sk])
                    sk += 1
                while nm != K - 1:
                    nm = wm.remove(A[sm])
                    sm += 1
                ans += sm - sk
                e += 1
        return ans

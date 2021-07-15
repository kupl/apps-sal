
from typing import Dict, Set, List, Tuple
from collections import defaultdict
from pprint import pprint


class Window:
    def __init__(self):
        self._counter = {}
        self._distinct_num = 0

    def add(self,num):
        if num in self._counter:
            self._counter[num] += 1
        else:
            self._distinct_num += 1
            self._counter[num] = 1

    def remove(self,num):
        self._counter[num] -= 1
        if self._counter[num] == 0:
            self._distinct_num -= 1
            del self._counter[num]

    @property
    def nums(self):
        return self._distinct_num



class Solution:
    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:

        w1 = Window()
        w2 = Window()
        x = y = z = 0
        # w1 中包含 A[x:z] 中所有的数字，而且 w1 中不重合的数字数量为 K
        # w2 中包含 A[y:z] 中所有的数字，而且 w2 中不重合的数字数量为 K - 1
        # if x <= i < y; then A[i:z] 中的不重合的数字数量为 K

        result = 0
        while z < len(A):
            w1.add(A[z])
            w2.add(A[z])
            z += 1

            while w1.nums > K:
                w1.remove(A[x])
                x += 1
            while w2.nums > K - 1:
                w2.remove(A[y])
                y += 1

            if w1.nums == K:
                assert w2.nums == K - 1

            result += (y-x)
        return result


from collections import Counter

class Solution:
    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
        window1 = Window()
        window2 = Window()
        res = 0
        left1, left2 = 0, 0

        for i in range(len(A)):
            window1.add(A[i])
            window2.add(A[i])
            while window1.size() > K:
                window1.remove(A[left1])
                left1 += 1
            while window2.size() > K-1:
                window2.remove(A[left2])
                left2 += 1
            res += left2 - left1
        return res


class Window:
    def __init__(self):
        self.counter = Counter()

    def add(self, x):
        self.counter[x] += 1

    def remove(self, x):
        self.counter[x] -= 1
        if self.counter[x] == 0:
            del self.counter[x]

    def size(self):
        return len(self.counter)

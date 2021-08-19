class Window:
    def __init__(self):
        self.counter = collections.Counter()

    def add(self, x):
        self.counter[x] += 1

    def remove(self, x):
        self.counter[x] -= 1
        if self.counter[x] == 0:
            self.counter.pop(x)

    def __len__(self):
        return len(self.counter)


class Solution:
    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
        window1 = Window()
        window2 = Window()
        left1, left2 = 0, 0
        result = 0

        for right, num in enumerate(A):
            window1.add(num)
            window2.add(num)

            # At most K distinct elements
            while len(window1) > K:
                window1.remove(A[left1])
                left1 += 1

            # At most K-1 distinct elements
            while len(window2) >= K:
                window2.remove(A[left2])
                left2 += 1

            # At most K - At most (K-1) will give you exact K elements
            result += left2 - left1

        return result

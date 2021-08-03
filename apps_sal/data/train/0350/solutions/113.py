class Window:
    def __init__(self):
        self.counter = Counter()
        self.unique = 0

    def add(self, value: int):
        self.counter[value] += 1
        if self.counter[value] == 1:
            self.unique += 1

    def remove(self, value: int):
        self.counter[value] -= 1
        if self.counter[value] == 0:
            self.unique -= 1


class Solution:
    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
        window1 = Window()
        window2 = Window()
        left1 = left2 = answer = 0

        for right in A:
            window1.add(right)
            window2.add(right)

            while window1.unique > K:
                window1.remove(A[left1])
                left1 += 1

            while window2.unique >= K:
                window2.remove(A[left2])
                left2 += 1
            answer += left2 - left1
        return answer

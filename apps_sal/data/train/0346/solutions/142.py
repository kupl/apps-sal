class Window:

    def __init__(self):
        self.odd = 0

    def add(self, value: int):
        if value % 2 == 1:
            self.odd += 1

    def remove(self, value: int):
        if value % 2 == 1:
            self.odd -= 1


class Solution:

    def numberOfSubarrays(self, A: List[int], k: int) -> int:
        window1 = Window()
        window2 = Window()
        left1 = left2 = answer = 0
        for right in A:
            window1.add(right)
            window2.add(right)
            while window1.odd > k:
                window1.remove(A[left1])
                left1 += 1
            while window2.odd >= k:
                window2.remove(A[left2])
                left2 += 1
            answer += left2 - left1
        return answer

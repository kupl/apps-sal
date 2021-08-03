'''
[inf,0]
[1,0]
'''


class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        index = float('inf')
        left = []
        for i in range(len(seats)):
            val = seats[i]
            if val == 1:
                index = i
                left.append(0)
            elif index == float('inf'):
                left.append(float('inf'))
            else:
                left.append(abs(i - index))
        index = float('inf')
        for i in range(len(seats) - 1, -1, -1):
            val = seats[i]
            if val == 1:
                index = i
                seats[i] = 0
            elif index == float('inf'):
                seats[i] = float('inf')
            else:
                seats[i] = abs(i - index)
        out = float('-inf')
        for i in range(len(seats)):
            temp = min(left[i], seats[i])
            out = max(out, temp)
        return out

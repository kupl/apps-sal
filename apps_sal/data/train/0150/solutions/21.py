class Solution:
    def partitionDisjoint(self, A: List[int]) -> int:
        minA = [A[0], ]
        for i in A[1:]:
            minA.append(max(i, minA[-1]))
        minB = [A[-1], ]
        for i in A[:-1][::-1]:
            minB.append(min(minB[-1], i))
        minB = minB[::-1]
        for i in range(1, len(A)):
            if minA[i - 1] <= minB[i]:
                return i

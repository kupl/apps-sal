import collections


class Solution:

    def carFleet(self, D: int, P: List[int], S: List[int]) -> int:
        T = [(D - P[i]) / S[i] for i in range(len(P))]
        sortedIdx = sorted(list(range(len(P))), key=lambda x: P[x])
        print(sortedIdx)
        stack = []
        for i in sortedIdx:
            while stack and T[stack[-1]] <= T[i]:
                stack.pop()
            stack.append(i)
            print(stack)
        return len(stack)

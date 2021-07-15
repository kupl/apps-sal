from collections import deque

class Solution:
    def oddEvenJumps(self, A: List[int]) -> int:
        size = len(A)
        if size < 2:
            return size
        oddNext = [-1] * size
        evenNext= [-1] * size
        def getNext(arr: list, nextArr: list):
            stack = deque()
            for index in arr:
                while stack and stack[-1] <= index:
                    nextArr[stack[-1]] = index
                    stack.pop()
                stack.append(index)
        indexes = sorted(list(range(size)), key = lambda i: A[i])
        getNext(indexes, oddNext)
        indexes = sorted(list(range(size)), key = lambda i: -A[i])
        getNext(indexes, evenNext)
        odds = [False] * size
        evens = [False] * size
        odds[size - 1] = True
        evens[size - 1] = True
        for index in range(size - 2, -1, -1):
            if evenNext[index] >= 0 and odds[evenNext[index]]:
                evens[index] = True
            if oddNext[index] >= 0 and evens[oddNext[index]]:
                odds[index] = True
        return sum([1 for isGood in odds if isGood])

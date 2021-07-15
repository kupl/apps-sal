import bisect

class Solution:
    def shortestSubarray(self, A: List[int], K: int) -> int:
        n = len(A)
        preSums = [0] * (n + 1)
        for i in range(n): 
            preSums[i + 1] = preSums[i] + A[i]
            
        dque = collections.deque()
        shortest = n + 1
        for i in range(n + 1):
            while dque and preSums[i] - preSums[dque[0]] >= K: 
                shortest = min(shortest, i - dque.popleft())
            while dque and preSums[i] <= preSums[dque[-1]]: 
                dque.pop()
            dque.append(i)
        return shortest if shortest <= n else -1

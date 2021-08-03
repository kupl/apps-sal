class Solution:
    def shortestSubarray(self, A: List[int], K: int) -> int:
        cumsum = itertools.accumulate(A)

        mono = collections.deque([(0, -1)])
        result = math.inf
        for ind, val in enumerate(cumsum):
            while mono and mono[-1][0] >= val:
                mono.pop()
            mono.append((val, ind))

            while val - mono[0][0] >= K:
                result = min(result, ind - mono.popleft()[1])

        if result == math.inf:
            return -1
        else:
            return result

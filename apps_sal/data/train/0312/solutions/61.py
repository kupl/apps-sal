class Solution:

    def shortestSubarray(self, A: List[int], K: int) -> int:
        prefix = [0] * (len(A) + 1)
        for i in range(len(A)):
            prefix[i + 1] = prefix[i] + A[i]
        ans = sys.maxsize
        deque = collections.deque([])
        for i in range(len(A) + 1):
            while deque and prefix[i] - prefix[deque[0]] >= K:
                ans = min(ans, i - deque[0])
                deque.popleft()
            while deque and prefix[i] <= prefix[deque[-1]]:
                deque.pop()
            deque.append(i)
        return ans if ans != sys.maxsize else -1

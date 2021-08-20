class Solution:

    def shortestSubarray(self, A: List[int], K: int) -> int:
        n = len(A)
        if n == 1:
            return -1 if A[0] < K else 1
        if any(A) >= K:
            return 1
        s = [0]
        for i in range(n):
            s.append(s[-1] + A[i])
        print(s)
        i = 0
        deque = []
        min_length = n + 1
        while i < n + 1:
            while len(deque) > 0 and s[deque[-1]] >= s[i]:
                deque.pop()
            while len(deque) > 0 and s[i] - s[deque[0]] >= K:
                k = deque.pop(0)
                min_length = min(min_length, i - k)
            deque.append(i)
            i += 1
        return min_length if min_length < n + 1 else -1

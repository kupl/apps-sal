from collections import deque
class Solution:
    def shortestSubarray(self, A: List[int], K: int) -> int:
        if not len(A):
            return -1
        A += [0]
        prefsum = [0]
        for n in A:
            prefsum.append(prefsum[-1] + n)
        ans = len(A) + 1
        deq = deque()
        for i in range(len(A)):
            while len(deq) and prefsum[i] - prefsum[deq[0]] >= K:
                ans = min(i - deq[0], ans)
                deq.popleft()
            while len(deq) and prefsum[i] <= prefsum[deq[-1]]:
                deq.pop()
            deq.append(i)
        if ans == len(A) + 1:
            return -1
        return ans

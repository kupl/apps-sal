from collections import deque


class Solution:
    def shortestSubarray(self, A: List[int], K: int) -> int:
        prefix_arr = [0]
        for i in range(len(A)):
            prefix_arr.append(prefix_arr[i] + A[i])

        deq = deque()
        result = len(A) + 1

        for i in range(len(prefix_arr)):
            while len(deq) > 0 and prefix_arr[i] < prefix_arr[deq[-1]]:
                deq.pop()
            deq.append(i)

            while len(deq) > 0 and prefix_arr[deq[-1]] - prefix_arr[deq[0]] >= K:
                result = min(result, deq[-1]-deq[0])
                deq.popleft()

        if result == len(A) + 1:
            return -1

        return result


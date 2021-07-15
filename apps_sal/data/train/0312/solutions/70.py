class Solution:
    def shortestSubarray(self, A: List[int], K: int) -> int:
        if K == 0:
            return 0
        if not A:
            return -1
        if len(A) == 1:
            if A[0] >= K:
                return 1
            return 0
        from collections import deque
        ret = float('inf')
        for element in A:
            if element >= K:
                return 1
        for i in range(1, len(A)):
            A[i] += A[i-1]
        current_ele = deque()
        current_ele.append((-1, 0))
        for i, element in enumerate(A):
            while current_ele and current_ele[-1][1] >= element:
                current_ele.pop()
            current_ele.append((i, element))
            while current_ele[-1][1] >= current_ele[0][1]+K:
                ret = min(ret, current_ele[-1][0]-current_ele[0][0])
                current_ele.popleft()
        return ret if ret != float('inf') else -1

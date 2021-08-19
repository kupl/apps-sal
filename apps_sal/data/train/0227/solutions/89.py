from collections import deque


class Solution:

    def longestOnes(self, A: List[int], K: int) -> int:
        substited_indexes = deque()
        start = 0
        best = 0
        index = 0
        while index < len(A):
            num = A[index]
            if num == 0:
                if K > 0:
                    K -= 1
                    A[index] = 1
                    substited_indexes.append(index)
                elif K == 0 and len(substited_indexes) == 0:
                    start = index + 1
                else:
                    start = substited_indexes.popleft()
                    A[start] = 0
                    start += 1
                    K += 1
                    continue
            index += 1
            best = max(best, index - start)
        return best

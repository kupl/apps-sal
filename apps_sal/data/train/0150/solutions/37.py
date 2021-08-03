class Solution:
    def partitionDisjoint(self, A: List[int]) -> int:
        n = len(A)

        partidx = 0
        left_max = A[0]
        seen_max = A[0]
        for i in range(1, n):
            seen_max = max(seen_max, A[i])
            if A[i] < left_max:
                partidx = i
                left_max = seen_max
        return partidx + 1

        # left = [0 for i in range(n)]
        # right = [0 for i in range(n)]
        # left[0], right[n-1] = A[0], A[n-1]
        # for i in range(1, n):
        #     left[i] = max(left[i-1], A[i])
        # for i in range(n-2, -1, -1):
        #     right[i] = min(right[i+1], A[i])
        # print(left, right)
        # for i in range(n-1):
        #     if left[i] <= right[i+1]:
        #         return i+1

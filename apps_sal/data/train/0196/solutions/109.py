class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        # Main idea: if we iterate over A twice to generate
        # a prefix array, then we can get subarrays in const
        # time by checking windows of size j - i <= len(A)

        # Once we have the prefix array, this problem reduces
        # to sliding window maximum (except we're looking for
        # the minimum). With the sliding window minimum, we
        # can then update the result with
        # result = max(result, curr_elem - minimum)

        from collections import deque
        dq = deque()
        prefix = [0]
        N = len(A)

        for _ in range(2):
            for elem in A:
                prefix.append(elem + prefix[-1])

        result = A[0]
        for i in range(len(prefix)):
            if dq and dq[0] < i - N:
                dq.popleft()
            if dq:
                result = max(result, prefix[i] - prefix[dq[0]])
            while dq and prefix[dq[-1]] > prefix[i]:
                dq.pop()
            dq.append(i)
        return result

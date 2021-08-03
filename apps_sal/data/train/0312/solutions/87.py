class Solution:
    def shortestSubarray(self, A: List[int], K: int) -> int:
        # Step 1: create a prefix (left) sum for the array
        n = len(A)
        if n == 0:
            return -1
        dp = [0] * (n + 1)  # dp[i] is the sum of A[0: i]
        for i in range(1, n + 1):
            dp[i] = dp[i - 1] + A[i - 1]

        # Step 2: iterate over a monotonic (increasing) queue, whenever a new
        # prefix sum is >= most left ele + K, left pop
        queue = collections.deque()
        queue.append((0, 0))  # First ele is the index, second ele in the dop array

        # The minimum of the sequence length
        res = (n + 1)

        for i in range(1, n + 1):
            # Check if dp[i] minus the left end is no less than K
            while queue:
                qi, qe = queue[0]
                if qe + K <= dp[i]:
                    res = min(res, i - qi)
                    queue.popleft()
                else:
                    break

            # Update the monotonic queue
            while queue:
                _, qe = queue[-1]
                if qe >= dp[i]:
                    queue.pop()
                else:
                    break
            queue.append((i, dp[i]))

        if res == (n + 1):
            return -1
        else:
            return res

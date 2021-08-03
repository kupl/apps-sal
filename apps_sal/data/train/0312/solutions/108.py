from collections import deque


class Solution:
    def shortestSubarray(self, A, K):
        possible_starts = deque([0])

        prefix_sums = [0 for i in range(len(A) + 1)]
        for i in range(len(A)):
            prefix_sums[i + 1] = prefix_sums[i] + A[i]

        shortest_found = len(A) + 1
        curr_sum = 0
        for i in range(len(A) + 1):
            while len(possible_starts) > 0 and prefix_sums[i] - prefix_sums[possible_starts[0]] >= K:
                shortest_found = min(shortest_found, i - possible_starts.popleft())
            while len(possible_starts) > 0 and prefix_sums[i] <= prefix_sums[possible_starts[-1]]:
                possible_starts.pop()
            possible_starts.append(i)
        return shortest_found if shortest_found <= len(A) else -1

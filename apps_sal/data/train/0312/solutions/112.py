from collections import deque


class Solution:
    def shortestSubarray(self, A: List[int], K: int) -> int:
        # prefix_sums[i] == sum(A[:i - 1])
        prefix_sums = [0]
        for num in A:
            prefix_sums.append(prefix_sums[-1] + num)

        shortest_length = math.inf
        # a deque of indices i_1, ..., i_k s.t. P[i_1] <= P[i_2] ...
        cands = deque()
        for i, prefix_sum in enumerate(prefix_sums):
            while len(cands) > 0 and prefix_sum <= prefix_sums[cands[-1]]:
                cands.pop()
            while len(cands) > 0 and prefix_sum - prefix_sums[cands[0]] >= K:
                shortest_length = min(shortest_length, i - cands.popleft())
            cands.append(i)

        return shortest_length if shortest_length != math.inf else -1

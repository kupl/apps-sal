class Solution:
    def shortestSubarray(self, nums: List[int], K: int) -> int:
        possible_lefts = deque([(0, -1)])
        shortest = float('inf')

        total = 0

        for right, num in enumerate(nums):
            total += num

            while possible_lefts and total - possible_lefts[0][0] >= K:
                shortest = min(shortest, right - possible_lefts.popleft()[1])

            while possible_lefts and possible_lefts[-1][0] > total:
                possible_lefts.pop()

            possible_lefts.append((total, right))

        return shortest if shortest != float('inf') else -1

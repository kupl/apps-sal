class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:

        left = self.shortestTails(arr, target, False)
        right = self.shortestTails(arr, target, True)

        mn = float('inf')
        for i in range(len(arr) - 1):
            if left[i][0] < float('inf') and right[i + 1][0] < float('inf'):
                mn = min(mn, left[i][0] + right[i + 1][0])

        return mn if mn < float('inf') else -1

    def shortestTails(self, arr, target, reverse):
        end = len(arr) - 1 if reverse else 0

        prefixSumMap = {
            0: len(arr) if reverse else -1
        }
        s = 0

        shortestAt = [None] * len(arr)
        shortest = (float('inf'), -1, -1)

        for _ in range(len(arr)):
            s += arr[end]

            diff = s - target
            if diff in prefixSumMap:
                start = prefixSumMap[diff]

                if abs(end - start) < shortest[0]:
                    shortest = (abs(end - start), start, end)

            shortestAt[end] = shortest

            prefixSumMap[s] = end
            end = end - 1 if reverse else end + 1
        return shortestAt

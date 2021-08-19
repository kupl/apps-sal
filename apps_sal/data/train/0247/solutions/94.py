class Solution:

    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        (start, ans, sum) = (0, float('inf'), 0)
        best = [float('inf')] * len(arr)
        best_so_far = float('inf')
        for i in range(len(arr)):
            sum += arr[i]
            while sum > target:
                sum -= arr[start]
                start += 1
            if sum == target:
                if start > 0 and best[start - 1] != float('inf'):
                    ans = min(ans, best[start - 1] + i - start + 1)
                best_so_far = min(best_so_far, i - start + 1)
            best[i] = best_so_far
        return -1 if ans == float('inf') else ans

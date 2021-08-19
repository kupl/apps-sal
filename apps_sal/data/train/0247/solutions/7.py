class Solution:

    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        n = len(arr)

        def get_min(arr):
            min_left = [float('inf')] * n
            window = 0
            l = 0
            for r in range(n):
                window += arr[r]
                while window > target:
                    window -= arr[l]
                    l += 1
                if window == target:
                    min_left[r] = r - l + 1
                if r > 0:
                    min_left[r] = min(min_left[r], min_left[r - 1])
            return min_left
        min_left = get_min(arr)
        min_right = get_min(arr[::-1])[::-1]
        best = float('inf')
        for i in range(1, n):
            best = min(best, min_left[i - 1] + min_right[i])
        return best if best < float('inf') else -1

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

        def get_min_right():
            min_right = [float('inf') for _ in range(n)]
            window = 0
            r = n - 1
            for l in range(n - 1, -1, -1):
                window += arr[l]
                while window > target:
                    window -= arr[r]
                    r -= 1
                if window == target:
                    min_right[l] = r - l + 1
                if l < n - 1:
                    min_right[l] = min(min_right[l], min_right[l - 1])
            return min_right
        min_left = get_min(arr)
        min_right = get_min_right()
        print(min_right[::-1])
        best = float('inf')
        for i in range(1, n):
            best = min(best, min_left[i - 1] + min_right[i])
        return best if best < float('inf') else -1

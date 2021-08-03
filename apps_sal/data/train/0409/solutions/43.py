class Solution:
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        if sum(arr) > 0:
            n = len(arr)
            s = (k * sum(arr)) % 1000000007
            l, r = [float('-inf') for _ in range(len(arr))], [float('-inf') for _ in range(len(arr))]
            ml, mr = float('inf'), float('inf')
            for i in range(len(arr)):
                l[i] = arr[i] + l[i - 1] if i > 0 else arr[0]
                ml = min(ml, l[i])
                r[n - i - 1] = arr[n - i - 1] + r[n - i] if i > 0 else arr[-1]
                mr = min(mr, r[n - i - 1])
            return s + (abs(ml) if ml < 0 else 0) + (abs(mr) if mr < 0 else 0)
        arr1 = arr + arr + arr
        arr = arr1
        print(arr)
        mx, n = float('-inf'), len(arr)
        left = [float('-inf') for _ in range(len(arr))]
        for i in range(len(arr)):
            left[i] = max(arr[i], arr[i] + left[i - 1]) if i > 0 else arr[0]
            mx = max(mx, left[i])
        print(left)
        return max(mx, 0)

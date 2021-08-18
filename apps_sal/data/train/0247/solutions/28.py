class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        n = len(arr)
        prefix = [float('INF')] * (n + 1)
        suffix = [float('INF')] * (n + 1)

        tmp = 0
        start = 0
        for i in range(n):
            if arr[i] == target:
                prefix[i + 1] = 1
            elif tmp + arr[i] < target:
                tmp += arr[i]
            else:
                tmp += arr[i]
                while tmp > target and start < i:
                    tmp -= arr[start]
                    start += 1
                if tmp == target:
                    prefix[i + 1] = i - start + 1

            prefix[i + 1] = min(prefix[i + 1], prefix[i])

        tmp = 0
        start = -1
        for i in range(-1, -n - 1, -1):
            if arr[i] == target:
                suffix[i] = 1
            elif tmp + arr[i] < target:
                tmp += arr[i]
            else:
                tmp += arr[i]
                while tmp > target and start > i:
                    tmp -= arr[start]
                    start -= 1
                if tmp == target:
                    suffix[i] = start - i + 1

            suffix[i] = min(suffix[i], suffix[i + 1])

        min_val = float('INF')
        for i in range(n):
            min_val = min(min_val, prefix[i] + suffix[i + 1])

        return min_val if min_val != float('INF') else -1

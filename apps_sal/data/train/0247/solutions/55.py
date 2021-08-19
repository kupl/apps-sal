class Solution:

    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        prefix = [0]
        d = {0: -1}
        for i in range(len(arr)):
            prefix.append(arr[i] + prefix[-1])
            d[prefix[-1]] = i
        ans = first = second = float('inf')
        for i in range(len(arr)):
            if prefix[i + 1] - target in d:
                first = min(first, i - d[prefix[i + 1] - target])
            if first < float('inf') and prefix[i + 1] + target in d:
                second = d[prefix[i + 1] + target] - i
                ans = min(ans, first + second)
        return -1 if ans == float('inf') else ans

class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        if not arr:
            return -1

        prefixes = [0] * len(arr)
        suffixes = [0] * len(arr)

        left = right = 0
        curr = 0
        min_len = float('inf')
        while right < len(arr):
            curr += arr[right]

            while curr >= target and left <= right:
                if curr == target:
                    l = right - left + 1
                    if l < min_len:
                        min_len = l

                curr -= arr[left]
                left += 1

            prefixes[right] = min_len
            right += 1

        left = right = len(arr) - 1
        curr = 0
        min_len = float('inf')
        while left >= 0:
            curr += arr[left]

            while curr >= target and left <= right:
                if curr == target:
                    l = right - left + 1
                    if l < min_len:
                        min_len = l

                curr -= arr[right]
                right -= 1

            suffixes[left] = min_len
            left -= 1

        min_len = float('inf')

        for i in range(len(arr) - 1):
            s = prefixes[i] + suffixes[i + 1]
            if s < min_len:
                min_len = s
        return min_len if min_len != float('inf') else -1

class Solution:

    def longestDupSubstring(self, S: str) -> str:
        n = len(S)
        nums = [ord(S[i]) - ord('a') for i in range(n)]

        def search(position):
            h = 0
            for i in range(position):
                h = (h * 26 + nums[i]) % 2 ** 32
            seen = {h}
            const = 26 ** position % 2 ** 32
            for start in range(1, n - position + 1):
                h = (h * 26 - nums[start - 1] * const + nums[start + position - 1]) % 2 ** 32
                if h in seen:
                    return start
                seen.add(h)
            return -1
        (left, right) = (1, n)
        while left <= right:
            pivot = (left + right) // 2
            if search(pivot) != -1:
                left = pivot + 1
            else:
                right = pivot - 1
        start = search(left - 1)
        return S[start:start + left - 1]

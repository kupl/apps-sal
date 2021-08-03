class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:

        arr = [abs(ord(sc) - ord(tc)) for sc, tc in zip(s, t)]
        max_len = 0
        left, right = 0, 0
        curr_sum = 0
        max_len = 0
        while(right < len(arr)):
            curr_sum += arr[right]
            while(left < len(arr) and curr_sum > maxCost):
                curr_sum -= arr[left]
                left += 1
            max_len = max(max_len, right - left + 1)
            right += 1
        return max_len

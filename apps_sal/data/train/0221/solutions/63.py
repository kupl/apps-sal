def check(arr, n, l, mod):
    p = pow(26, l, mod)
    window_hash = 0
    hash_set = set()
    for i in range(l):
        window_hash = (26 * window_hash + arr[i]) % mod
    hash_set.add(window_hash)

    for i in range(1, n - l + 1):
        window_hash = (window_hash * 26 - (arr[i - 1]*p) + arr[i + l - 1])%mod
        if window_hash in hash_set:
            return i
        hash_set.add(window_hash)

    return False


class Solution:
    def longestDupSubstring(self, S: str) -> str:
        
        n = len(S)
        min_length, max_length = 1, n
        ans, prev_len = 0, 0
        mod = (1 << 63) - 1
        nums = [ord(S[i]) - ord('a') for i in range(n)]

        while min_length <= max_length:
            mid_length = int((max_length + min_length)/2)
            start = check(nums, n, mid_length, mod)
            if start != False:
                if prev_len < mid_length:
                    ans = start
                    prev_len = mid_length
                min_length = mid_length + 1
            else:
                max_length = mid_length - 1
        
        return S[ans:ans + prev_len]


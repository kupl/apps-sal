class Solution:

    def maxVowels(self, s: str, k: int) -> int:
        l = 0
        r = 0
        v_set = {'a', 'e', 'i', 'o', 'u'}
        window_len = 0
        count = 0
        max_len = 0
        while r < len(s):
            if window_len < k:
                if s[r] in v_set:
                    count += 1
                window_len += 1
            else:
                print((window_len, count, s[r]))
                if count == k:
                    max_len = k
                    return max_len
                else:
                    max_len = max(count, max_len)
                    if s[l] in v_set:
                        count -= 1
                    l += 1
                    window_len -= 1
                    if s[r] in v_set:
                        count += 1
                    window_len += 1
            r += 1
        max_len = max(count, max_len)
        return max_len

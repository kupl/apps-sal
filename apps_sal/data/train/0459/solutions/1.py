class Solution:

    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        ls = len(s)
        (start, end, max_len) = (0, 0, 0)
        (char_map, cnt, cur_max_char) = ({}, 0, 0)
        while end < ls:
            if s[end] in char_map:
                char_map[s[end]] += 1
            else:
                char_map[s[end]] = 1
            cnt += 1
            if char_map[s[end]] > cur_max_char:
                cur_max_char = char_map[s[end]]
            if cnt - cur_max_char > k:
                char_map[s[start]] -= 1
                start += 1
                cnt -= 1
            else:
                max_len = max(max_len, cnt)
            end += 1
        return max_len

class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        from collections import defaultdict
        res = 0
        valid_str_freq = defaultdict(int)
        window_letter = {}
        left = 0
        right = 0
        for right in range(0, len(s), 1):
            # print(left, right)
            for i in range(left, right, 1):
                if right - i < minSize:
                    break
                valid_str = s[i:right]
                # print(i, right, valid_str)
                valid_str_freq[valid_str] += 1
                res = max(res, valid_str_freq[valid_str])

            # add right
            if s[right] not in window_letter:
                window_letter[s[right]] = 1
            else:
                window_letter[s[right]] += 1

            # check left
            while (len(window_letter) > maxLetters
                   or right - left + 1 > maxSize
                   ):
                window_letter[s[left]] -= 1
                if window_letter[s[left]] == 0:
                    del window_letter[s[left]]
                left += 1
        right += 1
        for i in range(left, right, 1):
            if right - i < minSize:
                break
            valid_str = s[i:right]
            # print(i, right, valid_str)
            valid_str_freq[valid_str] += 1
            res = max(res, valid_str_freq[valid_str])
        return res

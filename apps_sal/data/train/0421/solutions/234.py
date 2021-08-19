class Solution:

    def lastSubstring(self, s: str) -> str:
        if not s:
            return None
        max_char = max(s)
        max_idxs = []
        for i in range(len(s)):
            if s[i] == max_char:
                if not max_idxs or s[i - 1] != max_char:
                    max_idxs.append(i)
        max_idxs.append(len(s))
        max_substring = s[max_idxs[0]:max_idxs[1]]
        ans_idx = max_idxs[0]
        for i in range(1, len(max_idxs) - 1):
            cur = s[max_idxs[i]:max_idxs[i + 1]]
            if max_substring == cur[:len(max_substring)]:
                max_substring = max_substring + cur
                ans_idx = max_idxs[i - 1]
            elif max_substring < cur:
                max_substring = cur
                ans_idx = max_idxs[i]
        return s[ans_idx:]

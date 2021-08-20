class Solution:

    def lastSubstring(self, s: str) -> str:
        (slow, fast, length) = (0, 1, 0)
        while fast + length < len(s):
            if s[slow + length] == s[fast + length]:
                length += 1
            elif s[slow + length] > s[fast + length]:
                fast += length + 1
                length = 0
            else:
                slow = fast
                fast = slow + 1
                length = 0
        return s[slow:]

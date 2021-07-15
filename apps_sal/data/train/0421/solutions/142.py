class Solution:
    def lastSubstring(self, s: str) -> str:
        slow, fast, length = 0, 1, 0
        while fast + length < len(s):
            if s[slow+length] == s[fast+length]: #if equal, compare the next character
                length += 1
            elif s[slow+length] > s[fast+length]: #the slow character is higher than fast one, compare the next first character
                fast += (length + 1)
                length = 0
            else: #the fast character is higher than slow one, compare the next sub string
                slow = fast
                fast = slow + 1
                length = 0

        return s[slow:]


class Solution:
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """

        # This works it just exceeds time limit
        characters = {}
        separators = set([])

        for char in s:
            char_count = characters.get(char, 0)
            characters[char] = char_count + 1

        for char, count in characters.items():
            if count < k:
                separators.add(char)

        for i, char in enumerate(s):
            if char in separators:
                return max(self.longestSubstring(s[0:i].rstrip(char), k), self.longestSubstring(s[i + 1:].lstrip(char), k))

        return len(s)

class Solution:
    def longestPrefix(self, s: str) -> str:
        best = ''

        left = 0
        right = len(s) - 1

        hash_left = 0
        hash_right = 0

        while left < len(s) - 1 and right > 0:
            hash_left += ord(s[left])
            hash_right += ord(s[right])

            if hash_left == hash_right:
                if s[:left + 1] == s[right:]:
                    best = s[right:]

            left += 1
            right -= 1

        return best

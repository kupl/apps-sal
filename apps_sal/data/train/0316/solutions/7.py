class Solution:

    def longestPrefix(self, s: str) -> str:
        best = ''
        left = 0
        right = len(s) - 1
        left_s = ''
        right_s = ''
        hash_left = 0
        hash_right = 0
        while left < len(s) - 1 and right > 0:
            hash_left += ord(s[left])
            hash_right += ord(s[right])
            left_s += s[left]
            right_s = s[right] + right_s
            if hash_left == hash_right:
                if left_s == right_s:
                    best = left_s
            left += 1
            right -= 1
        return best

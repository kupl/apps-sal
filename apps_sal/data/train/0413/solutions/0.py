class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome) == 1:
            return ''
        for i, val in enumerate(palindrome):
            if val != 'a' and i != len(palindrome) // 2:
                return palindrome[:i] + 'a' + palindrome[i+1:]
            elif val == 'a' and i == len(palindrome) - 1:
                return palindrome[:-1] + 'b'


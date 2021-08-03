class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        for i in range(math.floor(len(palindrome) / 2)):
            if palindrome[i] != 'a':
                return palindrome[0:i] + 'a' + palindrome[i + 1:]
        if len(palindrome) == 1:
            return ''
        else:
            return palindrome[:-1] + 'b'

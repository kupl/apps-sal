class Solution:
    def isValid(self, s: str) -> bool:
        s = list(s)
        left = 0
        while len(s) > 2 and left < len(s)-2:
            if s[left:left+3] == ['a', 'b', 'c']:
                s.pop(left+2)
                s.pop(left+1)
                s.pop(left)
                left -= 2
            else:
                left += 1
        if s:
            return False
        else:
            return True


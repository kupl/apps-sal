class Solution:
    def isValid(self, s: str) -> bool:
        rtn =''
        for i,char in enumerate(s):
            if char == 'a':
                rtn = rtn[:i] + 'abc' + rtn[i:]
        return rtn == s
                    
#             aabcbc,...abcabcababcc


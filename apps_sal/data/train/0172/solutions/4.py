class Solution:
    def maxDiff(self, num: int) -> int:
        return self.findMax(num) - self.findMin(num)
        
    def findMax(self, num):
        s = str(num)
        org = None
        new_s = ''
        for c in s:
            if c == '9':
                new_s += c
                continue
            if org is None:
                org = c
            if c == org:
                new_s += '9'
            else:
                new_s += c
        return int(new_s)
    
    def findMin(self, num):
        s = str(num)
        org = None
        rep = None
        new_s = ''
        
        for i in range(len(s)):
            if s[i] == '0':
                new_s += s[i]
                continue
            if i == 0:
                if s[0] == '1':
                    new_s += s[0]
                else:
                    org = s[0]
                    rep = '1'
                    new_s += rep
            else:
                if org is None and s[i] != '1':
                    org = s[i]
                    rep = '0'
                    new_s += rep
                elif s[i] == org:
                    new_s += rep
                else:
                    new_s += s[i]
        
        return int(new_s)


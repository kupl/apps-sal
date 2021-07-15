from collections import Counter
class Solution:
    def checkIfCanBreak(self, s1, s2):
        dic_1 = Counter(s1)
        dic_2 = Counter(s2)
        
        return self.check(dic_1, dic_2) or self.check(dic_2, dic_1)
    
    def check(self, d1, d2):
        res = 0
        for i in 'abcdefghijklmnopqrstuvwxyz':
            res += d2[i] - d1[i]
            if res < 0 :
                return False
        return True


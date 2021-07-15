class Solution:
    def canConvertString(self, s: str, t: str, k: int) -> bool:
        if len(s) != len(t):
            return False
        
        alreadySeen = {}
        
        for i in range(len(s)):
            if s[i] != t[i]:
                difference = (ord(t[i]) - ord(s[i])) % 26
                
                if difference > k:
                    return False
                
                if difference not in alreadySeen:
                    alreadySeen[difference] = 1
                else:
                    newDifference = difference + alreadySeen[difference] * 26

                    if newDifference > k:
                        return False
                    else:
                        alreadySeen[difference] += 1
        
        return True


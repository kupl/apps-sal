class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        s1 = ''.join(sorted(s1))
        s2 = ''.join(sorted(s2))
        
        cnt1 = 0
        cnt2 = 0
        
        for i in range(len(s1)):
            if s1[i] >= s2[i]:
                cnt1 += 1
            
            if s2[i] >= s1[i]:
                cnt2 += 1
                
        print((cnt1, cnt2))
        return cnt1 == len(s1) or cnt2 == len(s2)


class Solution:
     def predictPartyVictory(self, senate):
         """
         :type senate: str
         :rtype: str
         """
         s = [1 if x == 'R' else 0 for x in senate]
         
         Rban = 0
         Dban = 0
         i = 0
         ban = False
         while True:
             if s[i] == -1: pass
             else:
                 if s[i] == 1:
                     if Dban > 0:
                         Dban -= 1
                         s[i] = -1
                         ban = True
                     else: Rban += 1
                 else:
                     if Rban > 0:
                         Rban -= 1
                         s[i] = -1
                         ban = True
                     else: Dban += 1
             
             i += 1
             if i == len(s):
                 i = 0
                 if not ban: break
                 else: ban = False
         
         if Rban > 0: return "Radiant"
         else: return "Dire"

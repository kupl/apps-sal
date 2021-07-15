class Solution:
     def predictPartyVictory(self, senate):
         """
         :type senate: str
         :rtype: str
         """
         r = collections.deque()
         d = collections.deque()
         for i,c in enumerate(senate):
             if c == "R":
                 r.append(i)
             else:
                 d.append(i)
         
         return self.eliminateSenators(r,d)
     
     def eliminateSenators(self,r,d):
         if len(r)==0: return "Dire"
         if len(d)==0:return "Radiant"
         
         r2 = collections.deque()
         d2 = collections.deque()
         
         while len(r)> 0 or len(d)>0:
             if len(r)==0:
                 if len(r2)==0:
                     return "Dire"
                 else:
                     r2.popleft()
                     d2.append(d.popleft())
             elif len(d)==0:
                 if len(d2)==0:
                     return "Radiant"
                 else:
                     d2.popleft()
                     r2.append(r.popleft())       
             else:
                 r_curr = r.popleft()
                 d_curr = d.popleft()
                 if r_curr < d_curr:
                     r2.append(r_curr)
                 else:
                     d2.append(d_curr)
         
         return self.eliminateSenators(r2,d2)      

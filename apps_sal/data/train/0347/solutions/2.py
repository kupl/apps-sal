class Solution:
     def checkInclusion(self, s1, s2):
         """
         :type s1: str
         :type s2: str
         :rtype: bool
         """
         
         if len(s2) < len(s1): return False
         counter = collections.defaultdict(int)
         for c in s1: counter[c] += 1
         
         seen = collections.defaultdict(int)
         
         for i in range(len(s1)-1):
             seen[s2[i]] += 1
 
         right = len(s1)-1
         while right < len(s2):
             seen[s2[right]] += 1
             if seen == counter: return True
             right += 1
             left = right - len(s1)
             seen[s2[left]] -= 1
             if seen[s2[left]] == 0: del seen[s2[left]]
                 
         return False
             


class Solution:
     def isMatch(self, s, p):
         """
         :type s: str
         :type p: str
         :rtype: bool
         """
         len_s = len(s)
         len_p = len(p)
         
         if len_s == 0 and len_p == 0:
             return True
         elif len_p == 0:
             return False
         elif len_p == p.count('*'):
             return True
         elif len_p - p.count('*') > len_s:
             return False
         
         i_s = 0
         i_p = 0
         star_index = None
         s_star_match = None
         
         while i_s < len_s:
             pchar = p[i_p] if i_p < len_p else None
             schar = s[i_s]
             if pchar == '*':
                 star_index = i_p
                 s_star_match = i_s
                 i_p += 1
             elif pchar == '?' or pchar == schar:
                 i_s +=1
                 i_p += 1
             elif star_index is not None:
                 i_p = star_index + 1
                 s_star_match += 1
                 i_s = s_star_match
             else:
                 return False
         while i_p < len_p and p[i_p] == '*':
             i_p += 1
         return i_p == len_p
         


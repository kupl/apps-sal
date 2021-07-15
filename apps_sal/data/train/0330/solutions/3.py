class Solution:
     def isNumber(self, s):
         """
         :type s: str
         :rtype: bool
         """
         states = [{},
                 {"blank": 1, "sign": 2, "dot": 4, "digit": 3},
                 {"digit": 3, "dot": 4},
                 {"digit": 3, "blank": 9, "e": 6, "dot": 5},
                 {"digit": 5},
                 {"digit":5, "e":6, "blank": 9},
                 {"sign": 7, "digit": 8},
                 {"digit": 8},
                 {"digit": 8, "blank": 9},
                 {"blank": 9}]
         
         curr_state = 1
         for c in s:
             type_c = self.checkType(c)
             if type_c not in states[curr_state].keys():
                 return False
             curr_state = states[curr_state][type_c]
         if curr_state not in [3, 5, 8, 9]:
             return False
         return True
 
     def checkType(self, c):
         if c == " ":
             return "blank"
         elif ord(c) >= ord("0") and ord(c) <= ord("9"):
             return "digit"
         elif c == ".":
             return "dot"
         elif c in ["E", "e"]:
             return "e"
         elif c in ["+", "-"]:
             return "sign"
         else:
             return "other"

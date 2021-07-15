class Solution:
     def isNumber(self, s):
         """
         :type s: str
         :rtype: bool
         """
         
         reg_sol = self.isNumber_regex(s)
         aut_sol = self.isNumber_automata(s)
         pyt_sol = self.isNumber_python(s)
         
         if not (reg_sol == aut_sol == pyt_sol):
             raise Exception("'{s}' is {reg_sol} according to regex, {aut_sol} according to automata, {pyt_sol} according to float()".format(s=s, reg_sol=reg_sol, aut_sol=aut_sol, pyt_sol=pyt_sol))
         
         return aut_sol
     
     def isNumber_regex(self, s):
 
         import re
 
         pattern = re.compile('^ *[-+]?([0-9]*\.[0-9]+|[0-9]+|[0-9]+\.)([eE][-+]?([0-9]+))? *$')
         return None != pattern.match(s)
     
     transition = (
         # 0
         {' ': 0,
          '.': 3,
          '-': 1,
          '0': 2},
         # 1
         {'.': 3,
          '0': 2},
         # 2
         {'0': 2,
          '.': 4,
          'e': 5,
          ' ': 8},
         # 3
         {'0': 4},
         # 4
         {'0': 4,
          'e': 5,
          ' ': 8},
         # 5
         {'-': 6,
          '0': 7},
         # 6
         {'0': 7},
         # 7
         {'0': 7,
          ' ': 8},
         # 8
         {' ': 8}
         )
     final_states = (2,4,7,8)
     
     def isNumber_automata(self, s):
         
         def key(char):
             if char in '\t':
                 return ' '
             if char in '123456789':
                 return '0'
             if char in 'E':
                 return 'e'
             if char in '+':
                 return '-'
             return char
         
         state = 0
         for i in s:
             try:
                 state = self.transition[state][key(i)]
             except KeyError:
                 return False
         return state in self.final_states
     
     def isNumber_python(self, s):
         try:
             f = float(s)
         except:
             return False
         else:
             return True
 
     def isNumber_manually(self, s):
         
         pass
         


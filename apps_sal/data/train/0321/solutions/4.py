class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        from collections import Counter
        def check_breakable(s1, s2):
          s1_counter = Counter(s1)
          s2_counter = Counter(s2)
          cnt = 0
          for char in 'abcdefghijklmnopqrstuvwxyz':
            cnt += s1_counter[char] - s2_counter[char]
            if cnt < 0:
              return False
          return True
        return check_breakable(s1, s2) == True or check_breakable(s2,s1) == True

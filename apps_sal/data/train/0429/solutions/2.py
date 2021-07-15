class Solution:
     def getHint(self, secret, guess):
         """
         :type secret: str
         :type guess: str
         :rtype: str
         """
         need = {}
         seen = {}
         ret_A = 0
         ret_B = 0
         for i in range(len(secret)):
             if secret[i] == guess[i]:
                 ret_A += 1
             else:
                 if seen.get(secret[i],0) > 0:
                     ret_B += 1
                     seen[secret[i]] -= 1
                 else:
                     need[secret[i]] = need.get(secret[i],0) + 1
                 if need.get(guess[i],0) > 0:
                     ret_B += 1
                     need[guess[i]] -= 1
                 else:
                     seen[guess[i]] = seen.get(guess[i],0) + 1
         return str(ret_A) + 'A' + str(ret_B) + 'B'


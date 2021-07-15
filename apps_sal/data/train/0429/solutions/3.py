class Solution:
     def getHint(self, secret, guess):
         """
         :type secret: str
         :type guess: str
         :rtype: str
         """
         dict, A, B = {}, 0, 0
         
         dicthash = {}
         for i in secret:
             if i in dicthash:
                 dicthash[i] += 1
             else:
                 dicthash[i] = 1
         
         for i in guess:
             if i in dicthash:
                 B += 1
                 if dicthash[i] == 1:
                     del dicthash[i]
                 else:
                     dicthash[i] -= 1
             
         for i, char in enumerate(list(secret)):
             if char == guess[i]:
                 A += 1
                 B -= 1
         
         return "{}A{}B".format(A, B)

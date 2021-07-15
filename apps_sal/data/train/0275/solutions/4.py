class Solution:
     def checkValidString(self, s):
         """
         :type s: str
         :rtype: bool
         """
         a=0
         b=0
         for i in range(len(s)) : #
             if s[i]== "*" : # The case of *
                 a = a+1 #To account for its possibility to be the opening of a brace pair
                 if b>0 : #To accout for its possibility to be the closing of a pair
                     b = b-1
 
             elif s[i]=="(" : #For each open brace you see, increment a and b (marking the potential to make a pair)
                 a = a+1
                 b = b+1
 
             elif s[i]==")" :
                 a = a-1 #For each ) brace, decrement a - marking one complete pair.
                 if b>0 : #This check is to ensure the terminating check - b==0 i.e. each ( has a pairing ).
                     b = b-1
 
             if a<0 : # If at any point the number of closing braces are more than opening braces, terminate
                 return False
 
         if b==0 : # If the number of pairs are balanced, return true
             return True
         else :
             return False

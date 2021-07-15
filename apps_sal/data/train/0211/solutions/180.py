# import math

# class Solution(object):
#     def maxUniqueSplit(self, s):
#         \"\"\"
#         :type s: str
#         :rtype: int
#         \"\"\"
#         account = 0
#         solutions = set()
#         account = self.findSolutions(s, solutions)
#         print(\"finished\")
#         print(solutions)
#         print(account)
        
#         # if substring are the same than the solution is not right
#         # if one solution has more substring than another adopt this one
#         # could use divide and conqure to go done a string
        
#     def findSolutions(self, s, solutions):
#         strLen = len(s)
#         if strLen != 1:
#             halfPoint = math.ceil(strLen / 2) # use floor so that the left side is always smaller string
#             leftSubStr = s[:halfPoint]
#             rightSubStr = s[halfPoint:]
#             print(\"strlength is: {} mid point : {} left string: {} right string: {} \".format(strLen, halfPoint, leftSubStr, rightSubStr))
#             # only keep spliting when the substring is unique in solutions
#             if leftSubStr not in solutions:
#                 # remove previous solution if it is in it
#                 solutions.add(leftSubStr)
#                 return self.findSolutions(leftSubStr, solutions) + 1
#                 solutions.remove(leftSubStr)

#             if rightSubStr not in solutions:
#                 solutions.add(rightSubStr)
#                 return account + self.findSolutions(rightSubStr, solutions) + 1
#                 solutions.remove(rightSubStr)

#         else:
#             print(s)
#             return 1
        
class Solution:
    book = set()
    def maxUniqueSplit(self, s):
        result = 0
        for i in range(1, len(s)+1): #go through all the length of sub strings from left to right
            curr = s[:i]
            if curr not in self.book:
                self.book.add(curr) # add a type of sub string if it is not in it
                result = max(result, 1 + self.maxUniqueSplit(s[i:]))
                self.book.remove(curr)
        return result

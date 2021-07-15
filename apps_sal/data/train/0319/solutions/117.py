class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        
        stoneN = len(stoneValue)
        totalScore = sum(stoneValue)
        
        dp = {}
        
        def play(i0, ARound):
            if i0 == stoneN:
                return 0
            if (i0, ARound) in dp:
                return dp[(i0, ARound)]
            if ARound:
                subAns = float('-inf')
                thisRoundScore = 0
                for j in range(i0, min(i0+3, stoneN)):
                    thisRoundScore += stoneValue[j]
                    subAns = max(subAns, thisRoundScore + play(j+1, False))
            else:
                subAns = float('inf')
                for j in range(i0, min(i0+3, stoneN)):
                    subAns = min(subAns, play(j+1, True))
            
            dp[(i0, ARound)] = subAns
            return subAns
        
        aScore = play(0, True) 
        bScore = totalScore - aScore
        # print(aScore, bScore)
        
        if aScore == bScore:
            return 'Tie'
        elif aScore > bScore:
            return 'Alice'
        else:
            return 'Bob'
        
#         AliceWinDict = {}
#         TieDict = {}
#         BobWinDict = {}
#         dp = {}
        
#         def play(i0, ARound, aScore, bScore):
#             if i0 == stoneN:
#                 if aScore == bScore:
#                     return 'Tie'
#                 elif aScore > bScore:
#                     return 'Alice'
#                 else:
#                     return 'Bob'
            
#             if (i0, ARound, aScore, bScore) in dp:
#                 return dp[(i0, ARound, aScore, bScore)]
            
#             if (i0, ARound) in TieDict:
#                 if aScore > TieDict[(i0, ARound)]:
#                     ans = 'Alice'
#                 elif aScore < TieDict[(i0, ARound)]:
#                     ans = 'Bob'
#                 return 'Tie'
#                 # ans = 'Tie'
#             else:
            
#                 if (i0, ARound) in AliceWinDict:
#                     if aScore >= AliceWinDict[(i0, ARound)]:
#                         return 'Alice'

#                 if (i0, ARound) in BobWinDict:
#                     if bScore >= BobWinDict[(i0, ARound)]:
#                         return 'Bob'

#                 if ARound:
#                     ans = None
#                     thisRoundScore = 0
#                     for j in range(i0, min(i0+3, stoneN)):
#                         thisRoundScore += stoneValue[j]
#                         subAns = play(j+1, False, aScore + thisRoundScore, bScore)

#                         if subAns == 'Alice':
#                             ans = 'Alice'
#                             break
#                         elif subAns == 'Tie':
#                             if ans == None:
#                                 ans = 'Tie'
#                     if ans == None:
#                         ans = 'Bob'
#                 else:
#                     ans = None
#                     thisRoundScore = 0
#                     for j in range(i0, min(i0+3, stoneN)):
#                         thisRoundScore += stoneValue[j]
#                         subAns = play(j+1, True, aScore, bScore + thisRoundScore)
#                         if subAns == 'Bob':
#                             ans = 'Bob'
#                             break
#                         elif subAns == 'Tie':
#                             if ans == None:
#                                 ans = 'Tie'
#                     if ans == None:
#                         ans = 'Alice'
                    
#             if ans == 'Tie':
#                 TieDict[(i0, ARound)] = aScore
                
#             elif ans == 'Alice':
#                 if (i0, ARound) in AliceWinDict:
#                     AliceWinDict[(i0, ARound)] = min(aScore, AliceWinDict[(i0, ARound)])
#                 else:
#                     AliceWinDict[(i0, ARound)] = aScore
                    
#             elif ans == 'Bob':
#                 if (i0, ARound) in BobWinDict:
#                     BobWinDict[(i0, ARound)] = min(bScore, BobWinDict[(i0, ARound)])
#                 else:
#                     BobWinDict[(i0, ARound)] = bScore   
                    
#             dp[(i0, ARound, aScore, bScore)] = ans
#             return ans
        
#         return play(0, True, 0, 0)


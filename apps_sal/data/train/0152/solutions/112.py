class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        n = len(position)
        if m == 2:
            return position[-1] - position[0]
        
        def checkPossible(ans0):
            preV = position[0]
            leftM = m - 1
            for num in position[1:]:
                if num - preV >= ans0:
                    leftM -= 1
                    preV = num
                    if leftM == 0:
                        return True
            return False
        
        l = 0
        r = position[-1]
        ans = position[1]-position[0]
        while r > l:
            mid = (r+l)//2
            # print(l, r, mid)
            if checkPossible(mid):
                ans = mid
                l = mid + 1
            else:
                r = mid
        return ans
        
#         dp = {}
#         minDelta = [position[i]-position[i-1] for i in range(1, n)]
#         # print(position)
#         # print(minDelta)
#         for i in range(n-3, -1, -1):
#             if minDelta[i] > minDelta[i+1]:
#                 minDelta[i] = minDelta[i+1]
        
#         def placeABall(preI, m0):
#             if (preI, m0) in dp:
#                 return dp[(preI, m0)]
#             if m0 == 1:
#                 return position[-1] - position[preI]
#             if n-preI-1 == m0:
#                 subAns = minDelta[preI]
#                 dp[(preI, m0)] = subAns
#                 return subAns
#             subAns = 0
            
#             l = preI+1
#             r = n-m0
#             if position[l] - position[preI] >= placeABall(l, m0-1):
#                 subAns = placeABall(l, m0-1)
#             elif position[r] - position[preI] <= placeABall(r, m0-1):
#                 subAns = position[r] - position[preI]
#             else:
#                 while l < r:
#                     m = (l+r)//2
#                     temp = placeABall(m, m0-1)
#                     if position[m] - position[preI] < temp:
#                         l = m + 1
#                     elif position[m] - position[preI] > temp:
#                         r = m
#                     else:
#                         l = m
#                         break
#                 subAns = (min(position[l] - position[preI], temp))
#                 if l + 1 <= n-m0:
#                     subAns = max(subAns, (min(position[l+1] - position[preI], placeABall(l+1, m0-1))))
#                 if l - 1 >= preI + 1:
#                     subAns = max(subAns, (min(position[l-1] - position[preI], placeABall(l-1, m0-1))))
                    
#             # for i1 in range(preI+1, n-m0+1):
#             #     subAns = max(subAns, min(position[i1] - position[preI], placeABall(i1, m0-1)))
#             dp[(preI, m0)] = subAns
#             return subAns
        
#         return placeABall(0, m-1)


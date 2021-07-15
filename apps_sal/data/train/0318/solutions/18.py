# class LinkedNode:
#     def __init__(self, val):
#         self.val = val
#         self.next = None
#         self.prev = None

class Solution:
    def maxSizeSlices(self, slices: List[int]) -> int:
        
        slicesN = len(slices)
        target = slicesN//3
        
        table1 = [[0 for i in range(slicesN)] for ti in range(target+1)]
        table2 = [[0 for i in range(slicesN)] for ti in range(target+1)]
        
        
        for ti in range(1, target + 1):
            for i in range(1, slicesN):
                if i == 1:
                    table1[ti][i] = slices[i]
                    table2[ti][i] = slices[i-1]
                    continue
                table1[ti][i] = max(table1[ti][i-1], table1[ti-1][i-2] + slices[i])
                table2[ti][i] = max(table2[ti][i-1], table2[ti-1][i-2] + slices[i-1])
        
        return max(table1[-1][-1], table2[-1][-1])
    
#         slicesN = len(slices)
#         table = [[] for _ in range(slicesN)]
#         target = slicesN//3
        
#         table[-1] = [slices[-1]]
#         table[-2] = [slices[-2]]
#         table[-3] = [slices[-3], slices[-3]+slices[-1]]
        
#         table2 = [[] for _ in range(slicesN)]

#         table2[-1] = [slices[-1]]
#         table2[-2] = [slices[-2]]
#         table2[-3] = [slices[-3]]
        
#         for i in range(slicesN-4, -1, -1):
#             table[i].append(slices[i])
#             table2[i].append(slices[i])
#             for j in range(i+2, slicesN):
#                 for k, sumTemp in enumerate(table[j]):
#                     if k+1 > target:
#                         break
#                     if k+1 >= len(table[i]):
#                         table[i].append(sumTemp + slices[i])
#                     else:
#                         table[i][k+1] = max(table[i][k+1], sumTemp + slices[i])
#                 for k, sumTemp in enumerate(table2[j]):
#                     if k+1 > target:
#                         break
#                     if k+1 >= len(table2[i]):
#                         table2[i].append(sumTemp + slices[i])
#                     else:
#                         table2[i][k+1] = max(table2[i][k+1], sumTemp + slices[i])   
#         target = slicesN//3
#         ans1 = 0
#         for i, sums in enumerate(table[1:]):
#             if len(sums) >= target:
#                 ans1 = max(ans1, sums[target-1])
         
#         ans2 = 0
#         for i, sums in enumerate(table2):
#             if len(sums) >= target:
#                 ans2 = max(ans2, sums[target-1])
#         return max(ans1, ans2)

            
        
#         @lru_cache
#         def takePizza(slices0):
#             # print(slices0)
#             n = len(slices0)
#             if n == 3:
#                 return max(slices0)
#             subAns = max(slices0[0] + takePizza(slices0[2:n-1]), slices0[n-1] + takePizza(slices0[1:n-2]))
#             for i in range(1, n-1):
#                 subAns = max(subAns, slices0[i] + takePizza(slices0[:i-1] + slices0[i+2:]))
#             return subAns

#         return takePizza(tuple(slices))
        
#         pointerDict = {}
#         head = LinkedNode(0)
#         preNode = head
        
#         for i, pizzaSlice in enumerate(slices):
#             newLN = LinkedNode(pizzaSlice)
#             pointerDict[newLN] = i
#             preNode.next = newLN
#             newLN.prev = preNode
#             preNode = newLN
            
#         preNode.next = head
#         head.prev = preNode
            
#         slicesN = len(slices)
#         fullMask = (1 << slicesN -1)
            
#         dp = {}
        
#         def takePizza(m0, leftOver):
            
#             if m0 in dp:
#                 return dp[m0]
#             subAns = 0
#             if leftOver == 3:
#                 subAns = 0
#                 pointer = head.next
#                 while pointer != head:
#                     subAns = max(subAns, pointer.val)
#                     # print(pointer.val, pointerDict[pointer])
#                     pointer = pointer.next 
#                 # print(subAns)
#                 dp[m0] = subAns
#                 return subAns            
#             pointer = head.next
#             while pointer != head:
#                 m1 = m0|(1<<pointerDict[pointer])
#                 if pointer.next == head:
#                     endPointer = head.next
#                     m1 |= (1<<pointerDict[head.next])
#                 else:
#                     endPointer = pointer.next
#                     m1 |= (1<<pointerDict[pointer.next])
#                 if pointer.prev == head:
#                     startPointer = head.prev
#                     m1 |= (1<<pointerDict[head.prev])
#                 else:
#                     startPointer = pointer.prev
#                     m1 |= (1<<pointerDict[pointer.prev])    
                
                
#                 if pointer.next == head or pointer.prev == head:  
#                     headPrev = head.prev
#                     headNext = head.next
#                     head.next = endPointer.next
#                     head.prev = startPointer.prev
#                     head.prev.next = head
#                     head.next.prev = head
#                     subAns = max(subAns, pointer.val + takePizza(m1, leftOver-3))
#                     head.prev = headPrev
#                     head.next = headNext
#                 else:
#                     startPointer.prev.next = endPointer.next
#                     endPointer.next.prev = startPointer.prev
#                     subAns = max(subAns, pointer.val + takePizza(m1, leftOver-3))
#                 startPointer.prev.next = startPointer
#                 startPointer.next.pre = startPointer                    
#                 pointer.prev.next = pointer
#                 pointer.next.prev = pointer
#                 endPointer.prev.next = endPointer
#                 endPointer.next.pre = endPointer 
                
#                 pointer = pointer.next
#             dp[m0] = subAns
#             return subAns
#         return takePizza(0, slicesN)
            
            
            
            
            


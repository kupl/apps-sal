class Solution:
    def countTriplets(self, A: List[int]) -> int:
        c = Counter(x & y for x in A for y in A)
        return sum(c[xy] for xy in c for z in A if xy & z == 0)
#         bitsOneDict = {\"@\": 20}
#         ans = 0
#         ALen = len(A)
#         for j, num in enumerate(A):
#             i = 0
#             pointer = bitsOneDict
#             while num > 0:
#                 if num & 1:
#                     if i not in pointer:
#                         pointer[i] = {}
#                     if \"@\" not in pointer:
#                         pointer[\"@\"] = i
#                     else:
#                         pointer[\"@\"] = max(i, pointer[\"@\"])
#                     pointer = pointer[i]
#                 num >>= 1
#                 i += 1
#             if \"$\" in pointer:
#                 pointer[\"$\"].add(j)
#             else:
#                 pointer[\"$\"] = set([j])
#             if \"@\" not in pointer:
#                 pointer[\"@\"] = i+1
#             else:
#                 pointer[\"@\"] = max(i+1, pointer[\"@\"])
                
#         for j1, num1 in enumerate(A):
#             for j2 in range(j1, ALen):
#                 num2 = A[j2]
#                 num12 = num1 & num2
#                 if num12 == 0:
#                     if j1 == j2:
#                         ans += ALen
#                     else:
#                         ans += ALen*2
#                 else:
#                     pointers = [bitsOneDict]
#                     i = 0          
#                     subAns = set()
#                     while i < 16:
#                         if num12 & 1 == 0:
#                             newPointers = []
#                             for k in range(len(pointers)-1, -1, -1):
#                                 pointer = pointers[k]
#                                 if i in pointer:
#                                     newPointers.append(pointer[i])
#                                 else:
#                                     if i > pointer[\"@\"]:
#                                         if \"$\" in pointer:
#                                             subAns |= pointer[\"$\"]
#                                         pointers.pop(k)   
#                             pointers += newPointers
#                         num12 >>= 1
#                         i += 1
#                     for pointer in pointers:
#                         if \"$\" in pointer:
#                             subAns |= pointer[\"$\"]
#                     if j1 == j2:
#                         ans += len(subAns)
#                     else:
#                         ans += len(subAns)*2
#         return ans


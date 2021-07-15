class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        # arr = {i:[1 for i in range(len(A))] for i in range(min(A)-max(A), max(A)-min(A)+1)}  # No need to initialize initially, will save lots of space
        arr = {}
        ans = 0
        for i in range(1, len(A)):
            for j in range(i):
                dif = A[i]-A[j]
                if not arr.get(dif):
                    arr[dif] = [1 for i in range(len(A))]
                arr[dif][i] = arr[dif][j] + 1
                ans = max(ans, arr[dif][i])
        
        # for x in arr:
        #     print(x, arr[x])
        
        return ans




# TLE
#         arr = {i:[1 for i in range(len(A))] for i in range(min(A)-max(A), max(A)-min(A)+1)}
#         ans = 0
#         for dif in range(min(A)-max(A), max(A)-min(A)+1):
#             for j in range(1, len(arr[0])):
#                 for k in range(j-1, -1, -1):
#                     if A[j]-A[k] == dif:
#                         arr[dif][j] = arr[dif][k] + 1
#                         ans = max(ans, arr[dif][j])
#                         break

#         # for x in arr:
#         #     print(x, arr[x])
#         return ans
        
                        


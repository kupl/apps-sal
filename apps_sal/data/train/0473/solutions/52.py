class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        
#         ans = 0
#         n = len(arr)

#         for i in range(n-1):
            
#             left, right = arr[i], 0

#             for j in range(i + 1, n):
        
#                 right ^= arr[j]
                
#                 if left == right:
#                     ans += (j - i)

#         return ans

        n = len(arr)
        c = 0
        for k in range(1,n):
            b=0
            for j in range(k, 0, -1):
                b = b^arr[j]
                a = 0
                for i in range(j-1, -1, -1):
                    a = a^arr[i]
                    #print(i, j, k, \"=>\", a, b)
                    if a==b:
                        c+=1
        return c


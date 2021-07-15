class Solution:
     def maximumSwap(self, num):
         arr = [int(c) for c in str(num)]
         n = len(arr)
         posmax = [0] * n
         posmax[-1] = n-1
         for i in range(n-2, -1, -1):
             if arr[i] > arr[posmax[i+1]]:
                 posmax[i] = i
             else:
                 posmax[i] = posmax[i+1]
         for i in range(n):
             if arr[i] == 9:
                 continue
             j = posmax[i]
             if arr[j] > arr[i]:
                 arr[i], arr[j] = arr[j], arr[i]
                 return int(''.join(map(str, arr)))
         return num
     


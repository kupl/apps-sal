class Solution:
     def monotoneIncreasingDigits(self, N):
         """
         :type N: int
         :rtype: int
         """
         
         arr = [int(ch) for ch in str(N)] # create array from number 1234 => [1,2,3,4]
         marker = len(arr)
         
         i = len(arr)-2
         while i >= 0:
             if arr[i] > arr[i+1]:
                 marker = i+1
                 arr[i] -= 1  
             i-=1
         
         while marker < len(arr):
             arr[marker] = 9
             marker += 1
         
         return int(''.join([str(num) for num in arr]))
         
         
 #         # any number 0..9 has always monotone increasing digits
 #         if N < 10:
 #             return N
         
 #         stack = []
         
 #         # create stack of digits 1234 -> [4,3,2,1]
 #         while N:
 #             stack.append(N%10)
 #             N = N // 10      
         
 #         X = 0
 #         power_of_10 = len(stack)-1
 #         right = stack.pop()
 #         while stack:
 #             left = right
 #             right = stack.pop()
 #             if left <= right:
 #                 X += left * (10**power_of_10)
 #                 power_of_10 -= 1
 #             else:
 #                 X += (left-1) * (10**power_of_10)
 #                 X += int('9'*power_of_10)
 #                 return self.monotoneIncreasingDigits(X)
         
 #         # remaining part
 #         X += right
         
 #         return X


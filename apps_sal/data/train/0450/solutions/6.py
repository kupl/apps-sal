class Solution:
     def validUtf8(self, data):
         """
         :type data: List[int]
         :rtype: bool
         """
         def numOfFollowingBytes(num):
             if 0 <= num <= 127:
                 return 0
             elif 192 <= num <= 223:
                 return 1
             elif 224 <= num <= 239:
                 return 2
             elif 240 <= num <= 247:
                 return 3
             else:
                 return -1
         
         def isFollowingByte(num):
             return 128 <= num <= 191
         
         if not data:
             return False
         
         i, n = 0, len(data)
         while i < n:
             bytesToFollow = numOfFollowingBytes(data[i])
             if bytesToFollow == -1:
                 return False
             
             i += 1
             if i + bytesToFollow > n:
                 return False
             
             for _ in range(bytesToFollow):
                 if not isFollowingByte(data[i]):
                     return False
                 i += 1
         
         return True

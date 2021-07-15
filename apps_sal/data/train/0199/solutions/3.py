class Solution:
     def longestConsecutive(self, nums):
         """
         :type nums: List[int]
         :rtype: int
         """
         
         # init dict, set default to 0
         length_dict = {key: 0 for key in nums}
         longest = 0
         
         for i in nums:
             #print("i = "+str(i))
             if length_dict[i]:
                 #print("skip "+str(i)) # already done
                 continue
             
             length = 1
             length_dict[i] = 1
             #print(length_dict)
             
             j = i + 1
             while j in length_dict:
                 #print("+:"+str(j))
                 length_dict[j] = 1
                 length += 1
                 j += 1
             
             j = i - 1
             while j in length_dict:
                 #print("-:"+str(j))
                 length_dict[j] = 1
                 length += 1
                 j -= 1
             
             longest = max(longest, length)
         
         return longest


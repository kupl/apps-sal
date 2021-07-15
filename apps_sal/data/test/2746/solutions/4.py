class Solution:
     def compareVersion(self, version1, version2):
         """
         :type version1: str
         :type version2: str
         :rtype: int
         """
         
         
         if version1 == version2:
             return 0
         else:
             version1_nums = version1.split('.')
             version2_nums = version2.split('.')
             len1, len2 = len(version1_nums), len(version2_nums)
             end = max(len1, len2 )
             version1_nums.extend([0]*(end - len1))
             version2_nums.extend([0]*(end - len2))
             for i in range(end):
                 if int(version1_nums[i]) < int(version2_nums[i]):
                     return -1
                 elif int(version1_nums[i]) > int(version2_nums[i]):
                     return 1
             return 0


class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        
        
        dict = {}
        for i in range(len(s)):
            for j in range(i+minSize, i+maxSize+1):
                # check if substr already in dict
                if j <= len(s):
                    substr = s[i:j]
                    if len(set(substr)) <= maxLetters:
                        if substr in dict:
                            dict[substr] += 1
                        else:
                            dict[substr] = 1

        # count max value of dict
        max_count = 0
        for k,v in list(dict.items()):
            max_count = max(max_count, v)

        return max_count
        
        
        # brute force - TLE
#         max_count = 0

#         for i in range(len(s)):
#             for j in range(i+minSize, i+maxSize+1):
#                 if j < len(s):
#                     substr = s[i:j]
#                     # print(\"checking substr: \", substr)
#                     # valid substring length
#                     if len(set(substr)) <= maxLetters:
#                         # checking first condition
#                         # do the function
#                         cc = self.count(substr, s, maxLetters)
#                         max_count = max(max_count, cc)

#         return max_count


#     def count(self, substr, s, maxLetters):
#         # print(\"\")
#         # print(\"substr passed: \", substr)

#         # return the countOcurrences
#         count_times = 0
#         j = len(substr)

#         for i in range(len(s)-j+1):
#             # print(\"comparing with s[i:i+j]: \", s[i:i+j])
#             if s[i:i+j] == substr:
#                 count_times += 1

#         return count_times


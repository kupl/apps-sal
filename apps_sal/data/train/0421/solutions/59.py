class Solution:
    def lastSubstring(self, s: str) -> str:
        # sort of like a sliding window, where length is substr / window size
        left, right, length = 0, 1, 0
        n = len(s)
        while right + length < n:
            # print(left, right, length)
            # print(s[left + length], s[right + length])
            if s[left + length] == s[right + length]:
                # substrings so far are the same
                length += 1
            elif s[left + length] > s[right + length]:
                # first substring is more optimal, capture entire
                # left substring + right substrings
                right += length + 1
                length = 0
            else:
                # right substring is more optimal
                # left = max(left + length + 1, right) # this is confusing
                left += length + 1
                # aabc
                # lr, length 1
                # lr, length 2 -> aa and ab -> advance to left + length + 1
                # aaabc
                # lr, length 3 -> aaa and aab -> 
                
                right = left + 1
                length = 0
                
        return s[left:]
        
        
        
        
        
        
        
        # this is slow..
#         n = len(s)
#         answer = \"\"
        
#         for i in range(n):
#             # can't hurt to just go all the way to the end of the string
#             answer = max(answer, s[i:])

#         return answer


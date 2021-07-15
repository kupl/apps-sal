class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        def helper(curr_set, s):
            if len(s) == 0:
                return len(s)
            max_split = 0
            for i in range(len(s)):
                if s[:i+1] not in curr_set:
                    # curr_set2 = set(curr_set)
                    curr_set.add(s[:i+1])
                    max_split = max(max_split, 1 + helper(curr_set, s[i+1:]))
                    curr_set.remove(s[:i+1])
            return max_split
        return helper(set(), s)
        
        
        
#         curr_set = set()
#         i,j = 0,1
#         while j<=len(s):
#             if s[i:j] not in curr_set:
#                 curr_set.add(s[i:j])
#                 print(s[i:j])
#                 i, j = j, j+1
#             else:
#                 j += 1
        
#         return len(curr_set)


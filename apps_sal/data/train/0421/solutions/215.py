class Solution:
    def lastSubstring(self, s: str) -> str:
        if not s:
            return None
        
        # get max char from s
        max_char = max(s)
        max_idxs = []
        
        # get all max_char indexs to append into max_idxs
        for i in range(len(s)):
            if s[i] != max_char:
                continue
            if not max_idxs or s[i - 1] != max_char:
                max_idxs.append(i)
                
        # also append the length of s into the max_idxs for compersion
        max_idxs.append(len(s))
        
        # initialize the temp max letter
        max_letter = s[max_idxs[0]:max_idxs[1]]
        ans_idx = max_idxs[0]
        # using for loop to compare with each shrot letter those leading by max_char
        for i in range(len(max_idxs) - 1):
            cur = s[max_idxs[i]:max_idxs[i + 1]]
            print(cur)
            if max_letter < cur:
                max_letter = cur
                ans_idx = max_idxs[i]
                
        return s[ans_idx:]

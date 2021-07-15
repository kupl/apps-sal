class Solution:
    def minSteps(self, s: str, t: str) -> int:
        s_dict = {}
        t_dict = {}
        res = 0
        for i in range(len(s)):
            if s[i] in s_dict:
                s_dict[s[i]] = s_dict[s[i]] + 1
            else:
                s_dict[s[i]] = 1
        
        for j in range(len(t)):
            if t[j] in t_dict:
                t_dict[t[j]] = t_dict[t[j]] + 1
            else:
                t_dict[t[j]] = 1
        
        print((s_dict, t_dict))
        
        for i in range(len(s)):
            if s[i] in t_dict and t_dict[s[i]] > 0:
                s_dict[s[i]] -= 1
                t_dict[s[i]] -= 1
        
        for key, value in list(s_dict.items()):
            if value > 0:
                res += value
                
        print((s_dict, t_dict))
        return res


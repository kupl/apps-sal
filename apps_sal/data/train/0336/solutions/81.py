class Solution:
    def minSteps(self, s: str, t: str) -> int:
        s_dict = {}
        t_dict = {}
        diff = 0
        for i in s:
            if(i in s_dict):
                s_dict[i] += 1
            else:
                s_dict[i] = 1

        for i in t:
            if(i in t_dict):
                t_dict[i] += 1
            else:
                t_dict[i] = 1

        for i in s:
            if(i in t_dict and t_dict[i] > 0):
                t_dict[i] -= 1

        for i in t_dict:
            diff += t_dict[i]

        return diff

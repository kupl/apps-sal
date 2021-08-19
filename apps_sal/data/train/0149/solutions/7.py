class Solution:

    def removeDuplicates(self, s: str, k: int) -> str:
        count = 1
        flag = 1
        last_idx = 0
        while 1:
            i = 0
            temp_s = s
            while i < len(s) - 1:
                if s[i] != s[i + 1]:
                    i = i + 1
                else:
                    last_idx = i
                    while 1:
                        if i + 1 == len(s):
                            break
                        elif s[i] == s[i + 1]:
                            count = count + 1
                            i = i + 1
                        else:
                            break
                    if count >= k:
                        s = s[:last_idx] + s[last_idx + k:]
                        i = last_idx
                    count = 1
            if temp_s == s:
                break
        return s

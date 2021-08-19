class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        l1 = [char for char in s1]
        l1.sort()
        l2 = [char for char in s2]
        l2.sort()
        strlen = len(s1)
        flag = 0
        for i in range(strlen):
            if l1[i] >= l2[i]:
                continue
            else:
                flag = 1
                break
        if flag:
            for i in range(strlen):
                if l1[i] <= l2[i]:
                    continue
                else:
                    return False
        return True
#         freqs1 = [0]*26
#         freqs2 = [0]*26
#         stringlen = len(s1)
#         for i in range(stringlen):
#             freqs1[ord(s1[i])-97]+=1
#             freqs2[ord(s2[i])-97]+=1
#         for i in range(26):
#             if freqs1[i]>=freqs2[i]:
#                 break
#         else:
#             return True
#         for i in range(26):
#             if freqs2[i]>=freqs1[i]:
#                 break
#         else:
#             return True
#         return False

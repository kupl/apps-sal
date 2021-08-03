# class Solution:
#     def lastSubstring(self, s: str) -> str:


#         stack = []
#         dic = {}
#         for i in 'abcdefghijklmnopqrstuvwxyz':
#             dic[ord(i)] = i
#         right = 0
#         while right < len(s):
#             if not stack:
#                 stack.append(ord(s[right]))
#             else:
#                 if ord(s[right]) > stack[0]:
#                     stack = []
#                 elif ord(s[right]) == stack[0]:
#                     index = 0
#                     while right + index < len(s) and index < len(stack):
#                         if ord(s[right+index]) > stack[index]:
#                             stack = []
#                             break
#                         elif ord(s[right+index]) < stack[index]:
#                             break

#                         index += 1
#                 stack.append(ord(s[right]))
#             right += 1


#         res = ''

#         for i in stack:
#             res += dic[i]

#         return res

class Solution:
    def lastSubstring(self, s: str) -> str:
        if not s:
            return None
        # get max char from s
        maxC, N = max(s), len(s)
        # get max char indexs to append into inds
        # only store the first ind for consecutive max chars
        inds = [i for i in range(N) if s[i] == maxC and (i == 0 or s[i - 1] != maxC)]
        maxind = inds[0]  # starting index of the max substring

        # using for loop to compare with each substring lead by max char
        for i in range(1, len(inds)):
            curind = inds[i]  # start index of current substring
            step = 0  # index pointer from start index
            # compare the current sub with the max sub string
            while curind + step < N:
                if s[curind + step] > s[maxind + step]:  # current sub larger than maxsub
                    maxind = curind
                    break
                elif s[curind + step] == s[maxind + step]:
                    step += 1
                else:  # s[curind+step]<s[maxind+step]: # current sub smaller than maxsub
                    break

        return s[maxind:]

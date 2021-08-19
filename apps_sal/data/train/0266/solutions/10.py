# class Solution:
#     def numSplits(self, s: str) -> int:
#         n = len(s)
#         output = 0
#         for i in range(1, n):
#             if len(set(s[:i])) == len(set(s[i:n])):
#                 output += 1
#             if len(set(s[:i])) > len(set(s[i:n])):
#                 break
#         return output

class Solution:
    def numSplits(self, s: str) -> int:
        n = len(s)
        output = 0
        dic = {}
        for i, x in enumerate(s):
            if not x in dic:
                dic[x] = [i, i]
            else:
                dic[x][1] = i
        # print(dic)
        for i in range(0, n - 1):
            left = 0
            right = 0
            for letter, indexes in list(dic.items()):
                if i >= indexes[0]:
                    left += 1
                if i + 1 <= indexes[1]:
                    right += 1
            if left == right:
                output += 1
        return output

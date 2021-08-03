class Solution:

    # Method 2 - Two Pointers
    def lastSubstring(self, s: str) -> str:
        i = 0
        j = i + 1
        result = s
        while j < len(s):
            if s[i] > s[j]:
                j += 1
                continue
            elif s[i] < s[j]:
                i = j
                j += 1
            else:

                step = 0
                while j + step < len(s) and s[i + step] == s[j + step]:
                    step += 1

                # print(j+step, len(s))
                if j + step == len(s):
                    return s[i:]
                if s[i + step] > s[j + step]:
                    j += 1
                    continue
                else:
                    i = j
                    j += 1
                # print(s[i:], i, j)

        return s[i:]


#     ## Method 1 - brute force (imroved)
#     def lastSubstring(self, s: str) -> str:
#         start = max(set(s))
#         result = \"\"
#         for i, char in enumerate(s):
#             # if i + len(result) > len(s):
#             #     break
#             if char == start:
#                 result = max(result, s[i:])

#         return result

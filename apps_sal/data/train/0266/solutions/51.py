class Solution:
    def numSplits(self, s: str) -> int:
        leftMap = {}
        rightMap = {}

        for j in range(len(s)):
            rightMap[s[j]] = rightMap.get(s[j], 0) + 1

        i = 0
        result = 0
        while (i < len(s) - 1):
            leftMap[s[i]] = leftMap.get(s[i], 0) + 1
            rightMap[s[i]] = rightMap[s[i]] - 1
            if (rightMap.get(s[i], 0) <= 0):
                rightMap.pop(s[i])

            if (len(leftMap) == len(rightMap)):
                result += 1
            i += 1
            # print(\"leftMap\", leftMap)
            # print(\"rightMap\", rightMap)

        return result

# method 2
#         prefix = [0] * len(s) # distinct number from s[0] to s[i]
#         suffix = [0] * len(s) # distinct number from s[len(s)-1] to s[i]
#         prefixMap = {}
#         suffixMap = {}
#         for i in range(len(s)):
#             j = len(s) - 1 - i
#             prefixMap[s[i]] = prefixMap.get(s[i], 0) + 1
#             suffixMap[s[j]] = suffixMap.get(s[j], 0) + 1
#             prefix[i] = len(prefixMap)
#             suffix[j] = len(suffixMap)

#         result = 0
#         k = 0
#         while (k < len(s)-1):
#             if (prefix[k] == suffix[k+1]):
#                 result += 1
#             k += 1
#         return result

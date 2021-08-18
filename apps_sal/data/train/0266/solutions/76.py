class Solution:
    def numSplits(self, s: str) -> int:
        result1 = [[s[0]]]
        result2 = [[s[-1]]]
        n = len(s)
        for i in range(1, len(s)):
            list1 = list(result1[i - 1])
            list2 = list(result2[i - 1])
            if s[i] not in list1:
                list1.append(s[i])
            if s[n - 1 - i] not in list2:
                list2.append(s[n - 1 - i])
            result1.append(list1)
            result2.append(list2)
        result = 0
        result2.reverse()
        for i in range(len(s) - 1):
            if len(result1[i]) == len(result2[i + 1]):
                result += 1
        return result

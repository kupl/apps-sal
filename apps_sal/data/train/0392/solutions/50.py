class Solution:

    def numWays(self, s: str) -> int:
        totalones = 0
        for i in range(len(s)):
            if s[i] == '1':
                totalones += 1
        if totalones % 3 != 0:
            return 0
        if totalones == 0:
            return (len(s) - 2) * (len(s) - 1) // 2 % (10 ** 9 + 7)
        (onesEachPart, waysFirstPart, waysSecondPart) = (totalones // 3, 0, 0)
        count = i = 0
        while count <= 2 * onesEachPart:
            if s[i] == '1':
                count += 1
            if count == onesEachPart:
                waysFirstPart += 1
            elif count == 2 * onesEachPart:
                waysSecondPart += 1
            i += 1
        return waysFirstPart * waysSecondPart % (10 ** 9 + 7)

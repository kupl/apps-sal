class Solution:
    def numWays(self, s: str) -> int:
        modv = 10**9 + 7
        countOne = 0
        for x in s:
            if x == '1':
                countOne += 1
        if countOne == 0:
            return (len(s) - 2) * (len(s) - 1) // 2 % modv
        if countOne % 3 != 0:
            return 0
        count = 0
        indexOfOne = []
        markIndexWhen = [countOne // 3, countOne // 3 + 1, countOne // 3 * 2, countOne // 3 * 2 + 1]
        for i in range(len(s)):
            if s[i] == '1':
                count += 1
                if count in markIndexWhen:
                    indexOfOne.append(i)
        return (indexOfOne[1] - indexOfOne[0]) * (indexOfOne[-1] - indexOfOne[-2]) % modv

class Solution:
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        secretDict = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}
        friendDict = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}
        bulls = 0
        cows = 0
        for s, g in zip(secret, guess):
            if s == g:
                bulls += 1
            else:
                secretDict[int(s)] += 1
                friendDict[int(g)] += 1
        for i in range(10):
            cows += min(secretDict[i], friendDict[i])
        return '{}A{}B'.format(bulls, cows)

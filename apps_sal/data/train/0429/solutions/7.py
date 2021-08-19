class Solution:
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """

        d1 = {}
        d2 = {}
        for i, c in enumerate(secret):
            if c not in d1:
                d1[c] = []
            d1[c].append(i)

        for i, c in enumerate(guess):
            if c not in d2:
                d2[c] = []
            d2[c].append(i)

        bulls, cows = 0, 0

        for k in d2:
            if k not in d1:
                continue
            curBulls = curCows = 0
            posGuess = d2[k]
            posSecret = d1[k]
            for p in posGuess:
                if p in posSecret:
                    curBulls += 1
            # print(curBulls)
            curCows = max(0, min(len(posGuess) - curBulls, len(posSecret) - curBulls))
            # print(curCows)
            bulls += curBulls
            cows += curCows
        return str(bulls) + 'A' + str(cows) + 'B'

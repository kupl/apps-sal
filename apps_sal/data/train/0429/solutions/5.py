class Solution:
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        bulls = cows = 0
        hist = [0] * 10
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bulls += 1
            else:
                hist[ord(secret[i]) - ord('0')] += 1
                if hist[ord(secret[i]) - ord('0')] - 1 < 0:
                    cows += 1
                hist[ord(guess[i]) - ord('0')] -= 1
                if hist[ord(guess[i]) - ord('0')] + 1 > 0:
                    cows += 1
        return str(bulls) + "A" + str(cows) + "B"

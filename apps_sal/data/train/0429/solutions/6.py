class Solution:

    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        bull = 0
        cow = 0
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bull += 1
                secret = secret[:i] + 'a' + secret[i + 1:]
                guess = guess[:i] + 'b' + guess[i + 1:]
        secret = ''.join(sorted(secret))
        guess = ''.join(sorted(guess))
        i = 0
        j = 0
        while i < len(guess) and j < len(guess):
            if secret[i] == 'a':
                break
            if guess[j] == 'b':
                break
            if secret[i] == guess[j]:
                cow += 1
                i += 1
                j += 1
                continue
            if secret[i] < guess[j]:
                i += 1
                continue
            if secret[i] > guess[j]:
                j += 1
                continue
        print((secret, guess))
        return str(bull) + 'A' + str(cow) + 'B'

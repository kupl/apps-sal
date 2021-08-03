class Solution:
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """

        bulls = 0
        mismatch_chars = collections.defaultdict(int)

        for secret_char, guess_char in zip(secret, guess):
            if secret_char == guess_char:
                bulls += 1
            else:
                mismatch_chars[secret_char] += 1

        cows = 0
        for secret_char, guess_char in zip(secret, guess):
            if secret_char != guess_char and mismatch_chars[guess_char] > 0:
                mismatch_chars[guess_char] -= 1
                cows += 1

        return '%sA%sB' % (bulls, cows)

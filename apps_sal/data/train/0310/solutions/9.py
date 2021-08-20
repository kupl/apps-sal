class Solution:

    def monotoneIncreasingDigits(self, N):
        N = str(N)
        L = len(N)
        for i in range(L - 1):
            if N[i] > N[i + 1]:
                return self.monotoneIncreasingDigits(int(N[:i] + str(int(N[i]) - 1) + '9' * (L - i - 1)))
        return int(N)

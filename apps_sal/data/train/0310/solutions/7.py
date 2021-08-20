class Solution:

    def monotoneIncreasingDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        a = list(str(N))
        i = 1
        while i < len(a) and a[i] >= a[i - 1]:
            i += 1
        while 0 < i < len(a) and a[i] < a[i - 1]:
            a[i - 1] = str(int(a[i - 1]) - 1)
            i -= 1
        a[i + 1:] = '9' * (len(a) - i - 1)
        return int(''.join(a))

class Solution(object):

    def monotoneIncreasingDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        l = list(str(N))
        length = len(l)
        for i in range(length):
            l[i] = ord(l[i]) - ord('0')
        index = -1
        for i in range(length - 1):
            if l[i] > l[i + 1]:
                index = i
                break
        if index == -1:
            return N
        j = -1
        for i in range(index, -1, -1):
            j = i
            if i > 0 and l[i] == l[i - 1]:
                continue
            break
        l[j] -= 1
        for i in range(j + 1, length):
            l[i] = 9
        res = 0
        for i in range(length):
            res = res * 10 + l[i]
        return res

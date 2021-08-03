class Solution:
    def nextGreaterElement(self, n):
        """
        :type n: int
        :rtype: int
        """
        nn = str(n)
        l = len(nn)
        if l < 2:
            return -1

        x = -1
        for i in range(l - 1, 0, -1):
            if nn[i] > nn[i - 1]:
                x = i - 1
                break

        if x == -1:
            return -1

        y = nn[x + 1]
        yy = x + 1
        for i in range(x + 1, l):
            if nn[i] > nn[x]:
                y = min(y, nn[i])
                if y == nn[i]:
                    yy = i

        left = nn[: x] + y
        right = nn[yy + 1: l] + nn[x] + nn[x + 1: yy]
        res = int(left + ''.join(sorted(right)))

        return res if res < 2 ** 31 else -1

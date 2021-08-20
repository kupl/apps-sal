class Solution:

    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        s = str(num)
        self.res = s

        def swap(i, j):
            (a, b) = (self.res[i], self.res[j])
            self.res = self.res[:i] + b + self.res[i + 1:]
            self.res = self.res[:j] + a + self.res[j + 1:]
        d = {}
        for (i, c) in enumerate(s):
            if c in d:
                d[c].append(i)
            else:
                d[c] = [i]
        c = 0
        for i in range(10)[::-1]:
            i = str(i)
            if i in d:
                arr = d[i]
                done = False
                for e in arr:
                    if e != c:
                        swap(c, arr[-1])
                        done = True
                        break
                    c += 1
                if done:
                    break
        return int(self.res)

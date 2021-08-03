class Solution:
    def maxUniqueSplit(self, s: str) -> int:

        self.mx = 0
        self.lim = len(s)

        def r(i, l, c):

            if i == self.lim - 1:

                if s[i] not in l:
                    if c + 1 > self.mx:
                        self.mx = c + 1
                else:
                    if c > self.mx:
                        self.mx = c
            else:
                for k in range(i + 1, self.lim + 1):
                    if k == self.lim:
                        if s[i:k] not in l:
                            if c + 1 > self.mx:
                                self.mx = c + 1
                    else:
                        if s[i:k] not in l:

                            r(k, l | {s[i:k]}, c + 1)

        r(0, set(), 0)
        return self.mx

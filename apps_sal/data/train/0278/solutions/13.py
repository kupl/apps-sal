class Solution:

    def largestMultipleOfThree(self, digits: List[int]) -> str:
        n = len(digits)
        f = [0] * 10
        for x in digits:
            f[x] += 1
        M = defaultdict(int)

        def upper(d, m):
            if f[d] < m:
                return 0
            return (f[d] - m) // 3 * 3 + m

        def mx(d, mod):
            dm = d % 3
            if dm == 0:
                return 0 if mod != 0 else f[d]
            if dm == 1:
                return upper(d, mod)
            if dm == 2:
                return upper(d, (3 - mod) % 3)
        for i in range(10):
            for j in range(3):
                M[i, j] = mx(i, j)
        X = [0] * 10
        R = [0] * 10

        def findout(i, mod):
            if i < 0:
                if mod == 0:
                    gt = False
                    sx = sr = 0
                    for i in range(10):
                        sx += X[i]
                        sr += R[i]
                    if sx > sr:
                        gt = True
                    elif sx == sr:
                        for i in reversed(list(range(10))):
                            if X[i] > R[i]:
                                gt = True
                                break
                            elif X[i] < R[i]:
                                break
                    if gt:
                        for i in range(10):
                            R[i] = X[i]
                return
            for j in range(3):
                if M[i, j] > 0:
                    X[i] = M[i, j]
                    findout(i - 1, (mod + j) % 3)
                    X[i] = 0
            findout(i - 1, mod)
        findout(9, 0)
        ret = ''
        for i in reversed(list(range(10))):
            if R[i] > 0:
                ret += R[i] * str(i)
        if len(ret) > 0 and ret[0] == '0':
            ret = '0'
        return ret

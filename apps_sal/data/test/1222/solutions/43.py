from sys import setrecursionlimit
setrecursionlimit(10**8)
k = int(input())
if k <= 10:
    print(k)
else:
    def dp(i):
        if i == 10:
            return 10
        N = str(dp(i - 1))
        ans = 0
        l = len(N)
        for j, n in enumerate(N[::-1]):

            if j == l - 1:
                if int(n) != 9:
                    x = int(n) + 1
                    ans = 0
                    l -= 1
                    while x != 0 and l >= 0:
                        ans += x * 10 ** l
                        x -= 1
                        l -= 1
                    return ans
                else:
                    return 10 ** l

            if n == "9":
                continue

            if int(N[l - j - 2]) - int(n) >= 0:
                ans = int(N[: l - j - 1]) * 10 ** (j + 1)
                l = j
                x = int(n) + 1
                while x != 0 and l >= 0:
                    ans += x * 10 ** l
                    x -= 1
                    l -= 1
                return ans
    print((dp(k)))

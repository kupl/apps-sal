from sys import stdin, stdout
def Pi(x): return stdout.write(str(x) + '\n')
def Ps(x): return stdout.write(str(x))
def S(x): return x * (x + 1) // 2
def I(x): return 1 + (2 * x)
def R(): return stdin.readline()
def Ri(x): return list(map(int, x.split()))
def Rs(x): return list(map(str, x.split()))
def Rf(x): return list(map(float, x.split()))


MaxN = int(1e5) + 10
# dp,A = []


def f(i, x, n, k, dp, A, B):
    if i == n:
        if x == 0:
            return 0
        return -1000000
    if dp[i][x + MaxN] != -1:
        return dp[i][x + MaxN]
    op1 = f(i + 1, x + A[i] - B[i] * k, n, k, dp, A, B) + A[i]
    op2 = f(i + 1, x, n, k, dp, A, B)
    dp[i][x + MaxN] = max(op2, op1)
    return dp[i][x + MaxN]


def main():
    # t = int(R())
    for x in stdin:
        n, x = Ri(x)
        A = list(Ri(R()))
        B = list(Ri(R()))
        dp = []
        for i in range(110):
            dp.append([-1] * (MaxN * 2))
        ans = f(0, 0, n, x, dp, A, B)
        if ans < 1:
            ans = -1
        Pi(ans)


def __starting_point():
    main()

# 60 == 360


__starting_point()

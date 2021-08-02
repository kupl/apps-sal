comb = [[0 for i in range(67)] for j in range(67)]

for i in range(67):
    comb[i][0], comb[i][i] = 1, 1
    for j in range(1, i):
        comb[i][j] = comb[i - 1][j - 1] + comb[i - 1][j]


def calc(x):
    cnt = 0
    digit = []
    while (x > 0):
        digit.append(x % 2)
        x //= 2
        cnt += 1
    ans, one = 0, 0
    for i in reversed(list(range(cnt))):
        if (digit[i] == 1):
            if (k - one >= 0):
                ans += comb[i][k - one]
            one += 1
    return ans


m, k = list(map(int, input().split()))

lcur, rcur = 0, 2 ** 64
while (lcur + 2 <= rcur):
    mid = (lcur + rcur) // 2
    if (calc(mid * 2) - calc(mid) < m):
        lcur = mid
    else:
        rcur = mid

print(rcur)

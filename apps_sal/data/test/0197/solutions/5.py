import sys
input = sys.stdin.readline

mod = 998244353
n = int(input())
LR = [list(map(int, input().split())) for i in range(n)]
RMIN = 1 << 31

ALL = 1
for l, r in LR:
    ALL = ALL * pow(r - l + 1, mod - 2, mod) % mod

for i in range(n):
    if LR[i][1] > RMIN:
        LR[i][1] = RMIN
    RMIN = min(RMIN, LR[i][1])

LMAX = -1
for i in range(n - 1, -1, -1):
    if LR[i][0] < LMAX:
        LR[i][0] = LMAX
    LMAX = max(LMAX, LR[i][0])

compression = []
for l, r in LR:
    compression.append(l)
    compression.append(r + 1)

compression = sorted(set(compression))
co_dict = {a: ind for ind, a in enumerate(compression)}

LEN = len(compression) - 1

if LEN == 0:
    print(0)
    return

DP = [[0] * LEN for i in range(n)]

for i in range(co_dict[LR[0][0]], co_dict[LR[0][1] + 1]):
    x = compression[i + 1] - compression[i]
    now = x
    # print(i,x)
    for j in range(n):
        if LR[j][0] <= compression[i] and LR[j][1] + 1 >= compression[i + 1]:
            DP[j][i] = now
        else:
            break
        now = now * (x + j + 1) * pow(j + 2, mod - 2, mod) % mod

# print(DP)

for i in range(1, n):
    SUM = DP[i - 1][LEN - 1]
    # print(DP)
    for j in range(LEN - 2, -1, -1):
        if LR[i][0] <= compression[j] and LR[i][1] + 1 >= compression[j + 1]:
            x = SUM * (compression[j + 1] - compression[j]) % mod
            now = x
            t = compression[j + 1] - compression[j]
            # print(x,t)

            for k in range(i, n):

                if LR[k][0] <= compression[j] and LR[k][1] + 1 >= compression[j + 1]:
                    DP[k][j] = (DP[k][j] + now) % mod
                else:
                    break
                now = now * (t + k - i + 1) * pow(k - i + 2, mod - 2, mod) % mod

        SUM += DP[i - 1][j]

print(sum(DP[-1]) * ALL % mod)

n, c = map(int, input().split())
X = []
for i in range(n):
    x, y = map(int, input().split())
    X.append((x, y))
SR, DR = [0] * (n + 1), [0] * (n + 1)
s, d = 0, 0
cur = 0
for i in range(n):
    x, y = X[i]
    SR[i + 1] = SR[i] + y - (x - cur)
    DR[i + 1] = DR[i] + y - 2 * (x - cur)
    cur = x

SL, DL = [0] * (n + 1), [0] * (n + 1)
s, d = 0, 0
cur = c
for i in reversed(range(n)):
    x, y = X[i]
    SL[n - i] = SL[n - 1 - i] + y - (cur - x)
    DL[n - i] = DL[n - 1 - i] + y - 2 * (cur - x)
    cur = x

for i in range(n):
    SL[i + 1] = max(SL[i + 1], SL[i])
    SR[i + 1] = max(SR[i + 1], SR[i])
ans = 0
for i in range(n + 1):
    a = max(DR[i] + SL[n - i], DL[i] + SR[n - i])
    ans = max(ans, a)
print(ans)

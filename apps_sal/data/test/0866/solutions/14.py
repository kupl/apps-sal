t = sorted(list(map(int, input().split())))
mod = 10 ** 9 + 7
X = t[0]
Y = t[1]
xy = 0
while X >= 0:
    if Y == 2 * X:
        break
    X -= 3
    Y -= 3
    xy += 1
if X < 0:
    print('0')
else:
    ans = 1
    for i in range(xy):
        ans = ans * (X + 2 * xy - i) * pow(i + 1, -1, mod) % mod
    print(ans)

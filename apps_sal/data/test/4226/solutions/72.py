X, Y = map(int, input().split())

ans = 0

if Y / 2 == X:
    ans = 1

for i in range(X + 1):
    j = X - i
    if Y == 2 * i + 4 * j:
        ans = 1

if ans == 1:
    print('Yes')
else:
    print('No')

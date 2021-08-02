N = int(input())
zolo = 0
for _ in range(N):
    d1, d2 = list(map(int, input().split()))
    if zolo >= 3:
        continue
    elif d1 == d2:
        zolo += 1
    else:
        zolo = 0

if zolo >= 3:
    print('Yes')
else:
    print('No')

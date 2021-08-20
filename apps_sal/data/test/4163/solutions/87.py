N = int(input())
tmp = 0
for i in range(N):
    (d1, d2) = map(int, input().split())
    if d1 == d2:
        tmp = tmp + 1
    else:
        tmp = 0
    if tmp == 3:
        break
if tmp == 3:
    print('Yes')
else:
    print('No')

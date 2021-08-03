n = int(input())
cnt = 0
for i in range(n):
    d1, d2 = map(int, input().split())
    if d1 == d2:
        cnt += 1
        if cnt == 3:
            break
    else:
        cnt = 0
if cnt >= 3:
    print('Yes')
else:
    print('No')

m, n = [int(x) for x in input().split(' ')]
raw = list(input())
p = 0
cnt = 1
prt = 0
while p < m - n - 1:
    for j in range(n):
        key = 0
        if raw[p + n - j] == "1":
            p = p + n - j
            cnt += 1
            key = 1
            break
        else:
            pass
    if key == 0:
        prt = 1
        break
if prt == 1:
    print(-1)
else:
    print(cnt)

n = int(input())
h = list(map(int, input().split()))

cnt = 0
for hh in range(1, max(h) + 1):
    flg = False
    for i in range(n):
        if h[i] >= hh:
            flg = True
        else:
            if flg:
                flg = False
                cnt += 1
    if flg:
        flg = False
        cnt += 1
print(cnt)

(h, w) = map(int, input().split())
n = int(input())
a = list(map(int, input().split()))
col = []
for i in range(n):
    for j in range(a[i]):
        col.append(i + 1)
cnt = 0
for i in range(h):
    p = col[cnt:cnt + w]
    if i % 2 == 0:
        print(*p)
    else:
        p = p[::-1]
        print(*p)
    cnt += w

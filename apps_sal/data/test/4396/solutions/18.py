n = int(input())
cnt = 0
for _ in range(n):
    (x, u) = map(str, input().split())
    if u == 'JPY':
        cnt += float(x)
    else:
        cnt += float(x) * 380000.0
print(cnt)

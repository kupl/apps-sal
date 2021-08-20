(n, m) = map(int, input().split())
a = list(map(int, input().split()))
cnt = 0
for i in range(len(a)):
    cnt += a[i]
    print(cnt // m, end=' ')
    cnt = cnt % m

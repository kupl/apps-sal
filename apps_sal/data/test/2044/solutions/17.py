n, m = map(int, input().split())
a = list(map(int, input().split()))
cnt = 0
for i in a:
    cnt += i
    print(cnt // m, end=' ')
    cnt %= m

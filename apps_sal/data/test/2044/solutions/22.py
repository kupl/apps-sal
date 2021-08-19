(n, m) = map(int, input().split())
copy = 0
a = list(map(int, input().split()))
for i in a:
    copy += i
    print(copy // m, end=' ')
    copy %= m

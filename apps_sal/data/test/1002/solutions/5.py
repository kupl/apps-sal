(n, d) = list(map(int, input().split()))
a = list(map(int, input().split()))
if sum(a) + (len(a) - 1) * 10 <= d:
    print((d - sum(a)) // 5)
else:
    print(-1)

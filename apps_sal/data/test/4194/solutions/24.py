(n, m) = map(int, input().split())
l = list(map(int, input().split()))
if sum(l) > n:
    print(-1)
else:
    print(n - sum(l))

(n, m) = map(int, input().split())
l = list(map(int, input().split()))
if n - sum(l) < 0:
    print('-1')
else:
    print(n - sum(l))

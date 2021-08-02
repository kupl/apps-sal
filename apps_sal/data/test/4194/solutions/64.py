n, m = tuple(map(int, input().split()))
x = list(map(int, input().split()))

for _ in x:
    n -= _

if n >= 0:
    print(n)
else:
    print(-1)

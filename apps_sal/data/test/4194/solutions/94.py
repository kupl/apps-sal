n, m = map(int, input().split())
days = input().split()

x = 0
for day in days:
    x = x + int(day)

if x <= n:
    print(n - x)
else:
    print(-1)

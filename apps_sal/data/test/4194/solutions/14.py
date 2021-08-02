n, m = list(map(int, input().split()))
a = list(map(int, input().split()))

day = 0

for i in range(m):
    day += a[i]

if day > n:
    print((-1))
else:
    print((n - day))

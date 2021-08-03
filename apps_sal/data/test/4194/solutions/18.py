n, m = map(int, input().split())
A = list(map(int, input().split()))

day = 0
for i in range(m):
    day = day + A[i - 1]

if n < day:
    print(-1)
else:
    ans = n - day
    print(ans)

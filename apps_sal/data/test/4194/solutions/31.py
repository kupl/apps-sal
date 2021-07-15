n, m = map(int, input().split())
A = list(map(int, input().split()))

day = 0
for i in range(len(A)):
    day = day + A[i-1]

if n < day:
    print(-1)
else:
    ans = n - day
    print(ans)

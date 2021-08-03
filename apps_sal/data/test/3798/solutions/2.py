def F(n, b):
    res = 0
    while n:
        n, m = divmod(n, b)
        res += m
    return res


N = int(input())
S = int(input())
if S > N:
    print(-1)
    return
if S == N:
    print(N + 1)
    return


inf = 10**18
ans = inf
d = 0
while True:
    d += 1
    lower = N // d
    upper = N // (d + 1) + 1
    if lower == upper:
        break
    FL = F(N, lower)
    FU = F(N, upper)
    if FL <= S <= FU:
        if (FU - S) % d == 0:
            pos = (FU - S) // d
            ans = min(ans, upper + pos)

for b in range(2, upper + 1):
    if F(N, b) == S:
        ans = min(ans, b)

if ans >= inf:
    print(-1)
else:
    print(ans)

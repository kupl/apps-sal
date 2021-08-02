n, k = list(map(int, input().split()))
c = list(map(int, input().split()))
cap = list(map(int, input().split()))

ans = 0
SUM = 0
FRE = [0] * n
for i in range(k):
    cap[i] -= 1
    SUM += c[cap[i]]
    FRE[cap[i]] = 1

tot = sum(c)

for i in range(n):
    if FRE[i] == 0:
        if FRE[(i + n - 1) % n] == 0:
            ans += c[i] * c[(i + n - 1) % n]
        if FRE[(i + n + 1) % n] == 0:
            ans += c[i] * c[(i + n + 1) % n]
        ans += c[i] * SUM
    else:
        ans += c[i] * (tot - c[i])

print(ans >> 1)

n = int(input())
S = list(input())
ans = 0
for i in range(1, n - 1):
    L = S[:i]
    R = S[i:]
    UL = set(L)
    UR = set(R)
    ans = max(ans, len(UL & UR))
print(ans)

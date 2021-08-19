(m, n) = list(map(int, input().split()))
pvar = 0
ans = 0
for i in range(1, m + 1):
    var = (i / m) ** n
    ans += i * (var - pvar)
    pvar = var
print(ans)

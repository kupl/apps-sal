(L, R) = map(int, input().split())
ls = list(range(L, min(L + 2019, R + 1)))
ans = 2019
for i in range(len(ls)):
    for j in range(i + 1, len(ls)):
        ans = min(ans, ls[i] * ls[j] % 2019)
print(ans)

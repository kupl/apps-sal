(L, R) = list(map(int, input().split()))
ans = 2 * 10 ** 9 + 1
for i in range(L, min(R, L + 2019) + 1):
    for j in range(i + 1, min(R, L + 2019) + 1):
        i %= 2019
        j %= 2019
        ans = min(ans, i * j % 2019)
print(ans)

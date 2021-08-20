(L, R) = map(int, input().split())
ans = 10 ** 10
for i in range(L, min(L + 2019, R + 1)):
    for j in range(i + 1, min(L + 2019, R + 1)):
        if ans > i * j % 2019:
            ans = i * j % 2019
print(ans)

N = int(input())
ans = [N for i in range(2 * N)]
for i in range(1, N + 1):
    x = i // 2 if i & 1 else N - 1 + i // 2
    y = x + N - i
    (ans[x], ans[y]) = (i, i)
print(*ans)

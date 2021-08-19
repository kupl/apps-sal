(N, M) = map(int, input().split())
p = (1 / 2) ** M
E = 1 / p
ans = (1900 * M + 100 * (N - M)) * E
ans = round(ans)
print(ans)

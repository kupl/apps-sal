N, M = map(int, input().split())
p = (1 / 2)**M

E = 0
for k in range(10**6):
    E += (1 - p)**k

ans = (1900 * M + 100 * (N - M)) * E
ans = round(ans)
print(ans)

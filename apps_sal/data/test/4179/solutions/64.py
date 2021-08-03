from operator import mul
ans = 0

N, M, C = map(int, input().split())
X = [list(map(int, input().split())) for i in range(N + 1)]

for i in range(N):
    num = list(map(mul, X[0], X[i + 1]))
    add = sum(num) + C
    if add > 0:
        ans += 1

print(ans)

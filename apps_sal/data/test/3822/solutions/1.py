n, L, v1, v2, k = list(map(int, input().split()))
n = (n + k - 1) // k * 2
dif = v2 - v1
p1 = (n * v2 - dif) * L
p2 = (n * v1 + dif) * v2
ans = p1 / p2
print(ans)


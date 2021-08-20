(_, n) = map(int, input().split())
M = {}
ans = 0
for x in map(int, input().split()):
    ans += M.get(x ^ n, 0)
    M[x] = M.get(x, 0) + 1
print(ans)

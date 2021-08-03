_, n = map(int, input().split())
M = {}
ans = 0
for x in map(int, input().split()):
    ans += M.get(x ^ n, 0)
    if x not in M:
        M[x] = 1
    else:
        M[x] += 1
print(ans)

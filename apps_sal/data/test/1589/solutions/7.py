(n, m) = [int(tmp) for tmp in input().split()]
ans = 0
for i in range(n):
    lvl = [int(tmp) for tmp in input().split()]
    for j in range(m):
        if lvl[2 * j] == 1 or lvl[2 * j + 1] == 1:
            ans += 1
print(ans)

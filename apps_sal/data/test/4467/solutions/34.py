n = int(input())
rs = [list(map(int, input().split())) for _ in range(n)]
bs = [list(map(int, input().split())) for _ in range(n)]
rs.sort(key=lambda x: x[1], reverse=True)
bs.sort()
ans = 0
for (c, d) in bs:
    for (a, b) in rs:
        if a < c and b < d:
            ans += 1
            rs.remove([a, b])
            break
print(ans)

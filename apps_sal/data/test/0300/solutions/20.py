n = int(input())
g = list(map(int, input().split()))

ans = 0
gr = sum(g) / n

while gr < 4.5:
    ma = min(g)
    i = g.index(ma)
    g[i] = 5
    gr = sum(g) / n
    ans += 1


print(ans)

d, g = map(int, input().split())
pc = [0] + [list(map(int, input().split())) for i in range(d)]
def dfs(d_, g_):
    if d_ == 0:
        return float("inf")
    cnt = min(g_ // (d_ * 100), pc[d_][0])
    cur = cnt * 100 * d_
    if cnt == pc[d_][0]:
        cur += pc[d_][1]
    if g_ > cur:
        cnt += dfs(d_ - 1, g_ - cur)
    return min(cnt, dfs(d_ - 1, g_))
print(dfs(d, g))

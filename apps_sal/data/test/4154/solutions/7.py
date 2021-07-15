n, m = map(int, input().split())
lr = [list(map(int, input().split())) for _ in range(m)]

INF = float('inf')
ans_l, ans_r = -INF, INF
for l, r in lr:
    ans_l = max(ans_l, l)
    ans_r = min(ans_r, r)
print(max(0, ans_r-ans_l+1))

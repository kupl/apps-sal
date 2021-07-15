N, K = map(int, input().split())

ans = 0
for x in range(2, 2*N+1):
    y = x - K
    if y<2 or y > 2*N:
        continue
    cnt_x = min(x-1, 2*N+1-x)
    cnt_y = min(y-1, 2*N+1-y)
    ans += cnt_x*cnt_y
print(ans)

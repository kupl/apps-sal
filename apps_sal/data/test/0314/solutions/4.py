n, k = map(int, input().split())

l = list(map(int, input().split()))

cnt = 0
ans = 0

for a in l:
    ans += 1
    cnt += a
    gt = min(8, min(cnt, k))
    k -= gt
    cnt -= gt
    if k == 0:
        print(ans)
        return

print(-1)

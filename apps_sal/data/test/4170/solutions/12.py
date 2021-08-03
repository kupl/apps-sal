N = int(input())
H = list(map(int, input().split()))
ans = 0
cnt = 0

pre = H[0]
for h in H[1:]:
    if h <= pre:
        cnt += 1
    else:
        ans = max(ans, cnt)
        cnt = 0
    pre = h
if cnt != 1:
    ans = max(ans, cnt)

print(ans)

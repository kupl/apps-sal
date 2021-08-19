n = int(input())
H = list(map(int, input().split()))
cnt = 0
ans = 0
tmp = H[0]
for h in H[1:]:
    if h <= tmp:
        cnt += 1
    ans = max(ans, cnt)
    if h > tmp:
        cnt = 0
    tmp = h
print(ans)

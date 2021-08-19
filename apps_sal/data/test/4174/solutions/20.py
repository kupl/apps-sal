(n, x) = map(int, input().split())
L = list(map(int, input().split()))
ans = 1
cnt = 0
for l in L:
    cnt += l
    if x >= cnt:
        ans += 1
print(ans)

(s, limit) = list(map(int, input().split()))
ans = []
for i in range(limit, 0, -1):
    k = i & (i ^ i - 1)
    if s >= k:
        s -= k
        ans.append(i)
if s:
    print(-1)
else:
    print(len(ans))
    print(*ans)

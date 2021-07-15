n,m = map(int,input().split())
cake = [[int(i) for i in input().split()] for _ in range(n)]
ans = 0
for i in range(2<<3):
    s = []
    for j in range(n):
        cnt = 0
        for k in range(3):
            if i>>k & 1: cnt += cake[j][k]
            else: cnt -= cake[j][k]
        s.append(cnt)
    s.sort(reverse=True)
    ans = max(ans, sum(s[:m]))
print(ans)

n = int(input())
l = sorted([(x[0] - x[1], x[0] + x[1]) for x in [list(map(int, input().split())) for _ in range(n)]], key=lambda x: x[1])
ans = 1; cur = 0
for i in range(1, n):
    if l[cur][1] <= l[i][0]:
        cur = i; ans += 1
print(ans)

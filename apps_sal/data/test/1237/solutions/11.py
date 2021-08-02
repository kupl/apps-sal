n, s = map(int, input().split())
d = []
for i in range(n):
    a, b = map(int, input().split())
    d.append((a, b))
d.sort(reverse=True)
ans = 0
curr = s
i = 0
while i < n:
    ans += (curr - d[i][0])
    curr = d[i][0]
    if d[i][1] > ans:
        ans = d[i][1]
    i += 1
print(ans + d[n - 1][0])

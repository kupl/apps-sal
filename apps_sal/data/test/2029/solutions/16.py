n, s = map(int, input().split())
ans = {}
for i in range(n - 1):
    a, b = map(int, input().split())
    if a in ans:
        ans[a].append(b)
    else:
        ans[a] = [b, ]
    if b in ans:
        ans[b].append(b)
    else:
        ans[b] = [a, ]

max_count = 0
for key in ans:
    if len(ans[key]) == 1:
        max_count += 1

if n == 2:
    print(s)
else:
    print(s / (max_count) * 2)

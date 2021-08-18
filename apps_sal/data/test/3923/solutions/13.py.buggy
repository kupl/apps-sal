from sys import stdin, stdout

n, a, b = map(int, input().split())
found = False
for x in range(n + 1):
    if (n - a * x) % b == 0:
        y = (n - a * x) // b
        if y >= 0:
            found = True
            break
if not found:
    print(-1)
    return
ans = []
l, r = 0, 1
for _ in range(x):
    l = r
    r = l + a
    for i in range(l, r):
        if i + 1 == r:
            ans.append(l)
        else:
            ans.append(i + 1)

for _ in range(y):
    l = r
    r = l + b
    for i in range(l, r):
        if i + 1 == r:
            ans.append(l)
        else:
            ans.append(i + 1)

print(*ans)

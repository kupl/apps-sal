import sys
n, x, y = map(int, input().split())
a = list(map(int, input().split()))
ans = 0
for i in range(n):
    d = False
    for j in range(max(i - x, 0), i):
        if a[j] < a[i]:
            d = True
            break
    if d:
        continue
    for j in range(i + 1, min(i + y + 1, n)):
        if a[j] < a[i]:
            d = True
            break
    if d:
        continue
    print(i + 1)
    return

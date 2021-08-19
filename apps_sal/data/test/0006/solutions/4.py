from math import ceil
t = int(input())
ans = []
for _ in range(t):
    (n, x) = map(int, input().split())
    a = -1
    b = 0
    for i in range(n):
        (d, h) = map(int, input().split())
        a = max(a, d - h)
        b = max(b, d)
    if x <= b:
        ans.append(1)
        continue
    elif a <= 0:
        ans.append(-1)
    else:
        x = x - b
        ans.append(ceil(x / a) + 1)
for el in ans:
    print(el)

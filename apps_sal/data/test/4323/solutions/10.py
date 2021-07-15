n, m = map(int, input().split())
a = []
b = []
for i in range(n):
    x, y = map(int, input().split())
    a.append(x)
    b.append(y)
if sum(b) > m:
    print(-1)
else:
    c = [a[i] - b[i] for i in range(len(a))]
    c.sort()
    s = sum(b)
    res = 0
    for i in c:
        if s + i <= m:
            res += 1
            s += i
        else:
            break
    print(n - res)

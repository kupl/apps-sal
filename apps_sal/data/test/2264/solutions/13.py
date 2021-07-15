t = int(input())
for i in range(t):
    n = int(input())
    a = []
    d = []
    for j in range(n):
        b, c = map(int, input().split())
        a.append(b)
        d.append(c)
    k1 = max(a)
    k2 = min(d)
    if k1 <= k2:
        print(0)
    else:
        print(k1 - k2)

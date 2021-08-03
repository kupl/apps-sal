n = int(input())
t = list(map(int, input().split()))
q, s = 0, sum(t)
if s % 3 == 0:
    a = s // 3
    b = s - a
    s = d = 0
    for i in range(n - 1):
        s += t[i]
        if s == b:
            q += d
        if s == a:
            d += 1
print(q)

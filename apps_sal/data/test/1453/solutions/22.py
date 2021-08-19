def f(a):
    n = len(a)
    s = [a[0]]
    for i in range(1, n):
        s.append(s[-1] + a[i])
    return s


(n, m) = [int(s) for s in input().split()]
a = sorted([0] + [int(s) for s in input().split()])
s1 = f(a)
for i in range(m, n + 1):
    s1[i] += s1[i - m]
for e in s1[1:]:
    print(e, end=' ')

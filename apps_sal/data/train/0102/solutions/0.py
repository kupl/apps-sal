s = []
for i in range(1, 10):
    k = 0
    for l in range(1, 10):
        k *= 10
        k += i
        s.append(k)
s.sort()
q = int(input())
while q:
    n = int(input())
    l = 0
    r = len(s)
    while l + 1 < r:
        m = (l + r) // 2
        if s[m] <= n:
            l = m
        else:
            r = m
    print(r)
    q -= 1

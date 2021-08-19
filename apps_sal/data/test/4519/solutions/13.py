q = int(input())
for _ in q * ' ':
    (n, k) = map(int, input().split())
    s = list(input())
    i = 0
    t = k
    c = 0
    while i < n and s[i] == '0':
        i += 1
        c += 1
    while i < n and k > 0:
        if s[i] == '0':
            u = min(i - c, k)
            k -= u
            (s[i], s[i - u]) = (s[i - u], s[i])
            c += 1
        i += 1
    print(*s, sep='')

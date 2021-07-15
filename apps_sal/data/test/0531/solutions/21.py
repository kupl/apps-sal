n = int(input())
l = list(map(int, input().split(' ')))
s = sum(l) // len(l)
mn, mx = min(l), max(l)
if mx - mn <= 1:
    print(n)
    for i in l:
        print(i, end=' ')
else:
    a, b, c = l.count(mn), l.count(mn + 1), l.count(mx)
    a1, b1, c1 = a - min(a, c), b + 2 * min(a, c), c - min(a, c)
    a2, b2, c2 = a + b // 2, b % 2, c + b // 2
    diff1 = min(a, a1) + min(b, b1) + min(c, c1)
    diff2 = min(a, a2) + min(b, b2) + min(c, c2)
    if diff1 <= diff2:
        print(diff1)
        s = (str(mn) + ' ') * a1 + (str(mn + 1) + ' ') * b1 + (str(mx) + ' ') * c1
        s = s[:-1]
        print(s)
    else:
        print(diff2)
        s = (str(mn) + ' ') * a2 + (str(mn + 1) + ' ') * b2 + (str(mx) + ' ') * c2
        s = s[:-1]
        print(s)

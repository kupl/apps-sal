n = int(input())
(s, e) = (0, 0)
c = True
w = dict()
for _ in range(n):
    (q, d) = input().split()
    if q == 'R':
        if c:
            s += 1
            c = False
        e += 1
        w[d] = e
    elif q == 'L':
        if c:
            e -= 1
            c = False
        s -= 1
        w[d] = s
    else:
        i = w[d]
        if i > e:
            i -= n
        print(min(e - i, i - s))

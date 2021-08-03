n, t = int(input()), input()
a, b = 'x', 'X'
k = t.count(a) - n // 2
if k:
    t = list(t)
    if k < 0:
        a, b, k = b, a, -k
    print(k)
    for i, c in enumerate(t):
        if c == a:
            t[i] = b
            k -= 1
            if k == 0:
                break
    print(''.join(t))
else:
    print('0\n' + t)

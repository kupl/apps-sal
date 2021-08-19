(l, r) = (-2000000000, 2000000000)
for x in range(int(input())):
    (t, n, a) = input().split()
    if t[0] == '>':
        n = int(n) + (len(t) == 1)
        if a == 'Y':
            l = max(l, n)
        else:
            r = min(r, n - 1)
    else:
        n = int(n) - (len(t) == 1)
        if a == 'Y':
            r = min(r, n)
        else:
            l = max(l, n + 1)
if l <= r:
    print((l + r) // 2)
else:
    print('Impossible')

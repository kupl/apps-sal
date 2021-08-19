(u, v) = (-2000000000, 2000000000)
for i in range(int(input())):
    (a, b, c) = input().split()
    k = int(b)
    if a == '>=':
        if c == 'Y':
            u = max(u, k)
        else:
            v = min(v, k - 1)
    elif a == '>':
        if c == 'Y':
            u = max(u, k + 1)
        else:
            v = min(v, k)
    elif a == '<=':
        if c == 'Y':
            v = min(v, k)
        else:
            u = max(u, k + 1)
    elif c == 'Y':
        v = min(v, k - 1)
    else:
        u = max(u, k)
print('Impossible' if u > v else u)

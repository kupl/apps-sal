q = int(input())
c = 0
L = []
while q > 0:
    q = q - 1
    (t, a, b) = input().split()
    a = int(a)
    b = int(b)
    if c == 0 and t == '+':
        (mi, ma) = (min(a, b), max(a, b))
        c = 1
    if t == '+':
        mi = max(mi, min(a, b))
        ma = max(ma, max(a, b))
    elif t == '?':
        if min(a, b) >= mi and max(a, b) >= ma:
            L.append('YES')
        else:
            L.append('NO')
print('\n'.join(L))

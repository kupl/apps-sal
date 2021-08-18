a, b = list(map(int, input().split()))
(a, b) = min(a, b), max(a, b)
if b < 2 * a:
    if a == b:
        print(0)
        return
    print((-a) % (b - a))
    return
s = [1]
q = b - a
for i in range(2, int((b - a)**(1 / 2) + 2)):
    while q % i == 0:
        t = [j * i for j in s]
        for aa in t:
            s.append(aa)
        s = list(set(s))
        q = q // i
if q != 1:
    t = [j * q for j in s]
    for aa in t:
        s.append(aa)
    s = list(set(s))
s.sort()
for i in s:
    if i >= a:
        print(i - a)
        return

def read(): return list(map(int, input().split()))


h1, a1, c1 = read()
h2, a2 = read()
ans = 1
a = []
ap = a.append
while h2 > a1:
    ans += 1
    if h1 > a2:
        h2 -= a1
        ap('STRIKE')
    else:
        h1 += c1
        ap('HEAL')
    h1 -= a2
ap('STRIKE')
print(ans)
print('\n'.join(a))

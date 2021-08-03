h1, a1, c1 = list(map(int, input().split()))
h2, a2 = list(map(int, input().split()))
res = []

while h2 > 0:
    if h1 <= a2 and h2 > a1:
        h1 += c1
        res.append('HEAL')
        h1 -= a2
    else:
        h2 -= a1
        res.append('STRIKE')
        h1 -= a2

print(len(res))
print('\n'.join(res))

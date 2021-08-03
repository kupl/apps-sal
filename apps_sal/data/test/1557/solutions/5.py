h1, a1, c1 = map(int, input().split())
h2, a2 = map(int, input().split())
cache = []
while h2 > 0:
    if h2 <= a1:
        h2 -= a1
        cache.append('STRIKE')
    elif h1 <= a2:
        h1 += c1
        cache.append('HEAL')
    else:
        h2 -= a1
        cache.append('STRIKE')
    h1 -= a2
print(len(cache))
for i in range(len(cache)):
    print(cache[i])

n, k = map(int, input().split())
s = input()
id1 = s.find('G')
id2 = s.find('T')
if abs(id1 - id2) % k:
    print("NO")
    return
coef = 1
if id2 < id1:
    coef = -1
while id1 != id2 and s[id1] in ('G', '.', 'T'):
    id1 += coef * k
if id1 == id2:
    print("YES")
else:
    print("NO")

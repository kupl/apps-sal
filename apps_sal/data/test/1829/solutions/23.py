def ri():
    return list(map(int, input().split()))


(n, m) = ri()
pol = set()
eny = set()
for i in range(n):
    pol.add(input())
for i in range(m):
    eny.add(input())
adding = 0
pol_copy = pol.copy()
for word in pol_copy:
    if word in eny:
        adding += 1
        eny.remove(word)
        pol.remove(word)
if adding % 2:
    adding = 1
else:
    adding = 0
if len(pol) + adding > len(eny):
    print('YES')
else:
    print('NO')

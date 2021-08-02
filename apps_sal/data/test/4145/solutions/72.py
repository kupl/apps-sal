x = int(input())

l = [2] + [i for i in range(3, 10**5 + 4, 2)]
p = 2
while p**2 < x:
    p = l[0]
    l = [q for q in l if q % p]
for p in l:
    if p >= x:
        print(p)
        break

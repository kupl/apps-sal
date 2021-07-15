h1, a1, c1 = [int(i) for i in input().split()]
h2, a2 = [int(i) for i in input().split()]
k = (h2 + a1 - 1) // a1
#print(k)
e = []
while k > 0:
    #print(k, h1, a2)
    if k == 1:
        e.append("STRIKE")
        break
    if h1 <= a2:
        e.append("HEAL")
        h1 += c1
    else:
        e.append("STRIKE")
        k -= 1
    h1 -= a2
print(len(e))
for el in e:
    print(el)


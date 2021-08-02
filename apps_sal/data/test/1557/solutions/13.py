h1, a1, c1 = list(map(int, input().split()))
h2, a2 = list(map(int, input().split()))

n = 0
l = []
while(h2 > 0):
    n += 1
    if (h2 - a1 <= 0):
        l.append(1)
        break
    if h1 - a2 <= 0:
        l.append(0)
        h1 += c1
        h1 -= a2
        continue
    else:
        l.append(1)
        h1 -= a2
        h2 -= a1

print(n)
for i in l:
    if i == 0:
        print("HEAL")
    else:
        print("STRIKE")

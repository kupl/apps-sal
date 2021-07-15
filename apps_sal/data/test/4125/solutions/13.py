import math

N, X = map(int, input().split())
x= list(map(int, input().split()))

absx = [abs(X - xx) for xx in x]
absx.sort()

divx0 = []

for i in range(math.ceil(math.sqrt(absx[0])), 0, -1):
    if absx[0] % i == 0:
        divx0.append(i)

t = []
for x in divx0:
    t.append(x)
    t.append(absx[0] // x)

divx0 = t
divx0.sort(reverse=True)

for dx0 in divx0:
    isok = True
    for xx in absx:
        if xx % dx0 != 0:
            isok = False
            break

    if isok:
        print(dx0)
        return

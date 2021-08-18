
AkshajK = input("").split()

p = int(AkshajK[0])
n = int(AkshajK[1])

c = 1
asdf = []
l_1 = []
for x in range(p):
    l_1.append(0)

while c <= n:
    s = int(input())
    if l_1[s % p] == 0:
        l_1[s % p] = 1
    else:
        asdf.append(c)
    c += 1
if asdf != []:
    print(asdf[0])
else:
    print(-1)

n = int(input())

l = []
for i in range(n):
    l.append(int(input()))

p = False

for i in range(2**n):
    k = ('0'*20 + str(bin(i))[2:])[-n:]

    total = 0
    for j in range(n):
        if (k[j] == '0'):
            total += l[j]
        else:
            total -= l[j]

    if (total%360 == 0):
        p = True

if p:
    print('YES')
else:
    print('NO')


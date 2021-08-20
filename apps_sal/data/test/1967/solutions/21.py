m = 0
l = input()
a = ''
b = ''
while l[m] != ' ':
    a = a + str(l[m])
    m += 1
a = int(a)
while m != len(l):
    b = b + str(l[m])
    m += 1
b = int(b)
h = 0
kartina = []
for lo in range(b):
    o = list(input())
    kartina.append(o)
for k in range(a):
    for t in range(b):
        print(kartina[t][k], end='')
        print(kartina[t][k], end='')
    print()
    for t in range(b):
        print(kartina[t][k], end='')
        print(kartina[t][k], end='')
    print()

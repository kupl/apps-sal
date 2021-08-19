n = int(input())
a = list(map(int, input().strip().split(' ')))
a.sort()
b = []
x = -1
c = 0
for i in a:
    if x == -1:
        x = i
        c = 1
    elif x == i:
        c += 1
    else:
        b.append((x, c))
        x = i
        c = 1
b.append((x, c))
n = len(b)
f = 0
for i in range(n):
    if b[i][1] % 2 == 1:
        f = 1
        print('Conan')
        break
if f == 0:
    print('Agasa')

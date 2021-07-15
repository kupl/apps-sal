a = []
a.append(input())
a.append(input())
a.append(input())
a.append(input())
b = []

for i in range(len(a)):
    b.append(len(a[i]) - 2)

b.sort()

res = []

if b[0] * 2 <= b[1] and b[1] != 0:
    res.append(b[0])

if b[2] * 2 <= b[3] and b[3] != 0:
    res.append(b[3])


if len(res) == 1:
    for i in range(len(a)):
        if len(a[i]) - 2 == res[0]:
            print(a[i][:1])
else:
    print('C')

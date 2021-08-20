q = int(input())
a = [False for i in range(0, 1002)]
s = []
for i in range(0, q):
    s.append(list(map(int, input().split())))
for i in s:
    for j in i:
        a[j] = True
if q == 2:
    for i in s[0]:
        for j in s[1]:
            (a[i * 10 + j], a[j * 10 + i]) = (True, True)
if q == 3:
    for i in s[0]:
        for j in s[1]:
            (a[i * 10 + j], a[j * 10 + i]) = (True, True)
    for i in s[0]:
        for j in s[2]:
            (a[i * 10 + j], a[j * 10 + i]) = (True, True)
    for i in s[1]:
        for j in s[2]:
            (a[i * 10 + j], a[j * 10 + i]) = (True, True)
    for i in s[0]:
        for j in s[1]:
            for k in s[2]:
                (a[k * 100 + i * 10 + j], a[k * 100 + j * 10 + i]) = (True, True)
                (a[k * 10 + i * 100 + j], a[k + j * 10 + i * 100]) = (True, True)
                (a[k + i * 10 + j * 100], a[k * 10 + i + j * 100]) = (True, True)
z = 0
while a[z + 1]:
    z += 1
print(z)

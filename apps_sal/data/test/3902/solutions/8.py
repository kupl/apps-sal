s = (input())
n = len(s)
x = set()

a = [[0 for i in range(2)] for j in range(n+3)]
b = [0 for i in range(n+3)]

b[n] = 1
a[n][0] = 1
a[n][1] = 1

for i in range(n - 1, 4, -1):
    if b[i + 2]:
        if a[i + 2][0] and (s[i:i + 2] != s[i + 2:i + 4]):
            b[i] = 1
            a[i][0] = 1
        if a[i + 2][1]:
            b[i] = 1
            a[i][0] = 1
        if b[i]:
            x.add(s[i:i + 2])
    if b[i + 3]:
        if a[i + 3][1] and (s[i:i + 3] != s[i + 3:i + 6]):
            b[i] = 1
            a[i][1] = 1
        if a[i + 3][0]:
            b[i] = 1
            a[i][1] = 1
        if b[i]:
            x.add(s[i:i + 3])

x = sorted(list(x))
print(len(x))
for i in x:
    print(i)


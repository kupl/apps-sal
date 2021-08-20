n = int(input())
z = []
res = n
for i in range(n):
    s = input().split()
    j = 0
    t = True
    while t and j < n:
        if s[j] == '1' or s[j] == '3':
            t = False
            res -= 1
        j += 1
    z.append(t)
print(res)
s = ''
for i in range(len(z)):
    if z[i]:
        s += str(i + 1) + ' '
print(s)

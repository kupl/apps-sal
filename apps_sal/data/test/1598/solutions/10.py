a = input()
a = list(a)
l = []
for i in range(0, len(a)):
    l.append([a[i], i])
i = 1
while i < len(l):
    if l[i][0] == '0' and l[i - 1][0] == '1':
        l.pop(i)
        l.pop(i - 1)
        i -= 2
    if i == -1:
        i = 0
    i += 1
for i in range(0, len(l)):
    a[l[i][1]] = 0
print(*a, sep='')

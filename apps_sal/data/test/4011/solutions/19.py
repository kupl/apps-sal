n = int(input())
a = list(input())
d = dict()
s = input().split()
can = set()
for i in range(9):
    if i < int(s[i]):
        can.add(str(i + 1))
    d[str(i + 1)] = s[i]
for i in range(n):
    if a[i] < d[a[i]]:
        a[i] = d[a[i]]
        i += 1
        while i < n and a[i] in can:
            a[i] = d[a[i]]
            i += 1
        break
print(*a, sep='')

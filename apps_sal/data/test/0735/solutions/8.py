__author__ = 'Gleb'
n = int(input())
a = input().split()
isna = []
for i in range(n):
    a[i] = int(a[i])
    isna.append(a[i])
a.sort()
i = 0
while i < n and isna[i] == a[i]:
    i += 1
nach = i
if i == n:
    print('yes')
    print(1, 1)
else:
    nache = isna[i]
    while i < n and (not a[i] == nache):
        i += 1
    kon = i
    b = isna[0:nach]
    for i in range(kon, nach - 1, -1):
        b.append(isna[i])
    b += isna[kon + 1:n]
    if b == a:
        print('yes')
        print(nach + 1, kon + 1)
    else:
        print('no')

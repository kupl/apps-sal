l = input().split()
n = int(l[0])
x = int(l[1])
l = input().split()
li = [int(i) for i in l]
mina = li[0]
ind = 0
for i in range(1, n):
    if li[i] <= mina:
        ind = i
        mina = li[i]
indexofx = x - 1
for i in range(n):
    if li[(indexofx + n - i) % n] == mina:
        ind = (indexofx + n - i) % n
        break
quot = li[ind]
indexofx = x - 1
if indexofx >= ind:
    rem = indexofx - ind
else:
    rem = n - 1 - ind + indexofx + 1
l = [0 for i in range(n)]
for i in range(n):
    if i != ind:
        l[i] = li[i] - quot
l[ind] = quot * n + rem
for i in range(1, rem + 1):
    l[(ind + i) % n] -= 1
for i in l:
    print(i, end=' ')
print()

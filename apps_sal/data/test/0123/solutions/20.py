input()
a = list(map(int, input().split()))
b = list(map(int, input().split()))
n = len(a)
k = len(b)

b.sort()

i = k - 1
c = []
for e in a:
    if e == 0:
        c.append(b[i])
        i -= 1
    else:
        c.append(e)

yes = False

for i in range(1, n):
    if c[i] < c[i - 1]:
        yes = True

if yes:
    print("Yes")
else:
    print("No")

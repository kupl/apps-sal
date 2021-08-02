n = int(input())
a = list(map(int, input().split()))
a.sort()
for i in range(n):
    if a[i] != 0:
        a = a[i:n]
        break

l = len(a)
c = [0] * l
c[0] = 1
for i in range(1, l):
    if a[i] != a[i - 1]:
        c[i] = 1
    else:
        c[i] = c[i - 1] + 1

if l == a.count(0):
    print(0)
elif c.count(1) + c.count(2) != l:
    print(-1)
else:
    print(c.count(2))

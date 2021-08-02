import bisect
n = int(input())
a = sorted(list(map(int, input().split())))
b = sorted(list(map(int, input().split())))
c = sorted(list(map(int, input().split())))
bl = [0] * n
blli = [0] * n
al = [0] * n
alli = [0] * n

for i in range(n):
    bl[i] = n - bisect.bisect(c, b[i])

blli[0] = sum(bl)
for i in range(n - 1):
    blli[i + 1] = blli[i] - bl[i]

for i in range(n):
    al[i] = n - bisect.bisect(b, a[i])

for i in range(n):
    if al[i] != 0:
        alli[i] = blli[-al[i]]

print(sum(alli))

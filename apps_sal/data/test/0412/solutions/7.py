n = int(input())
a = list(map(int, input().split()))
r = 0
k = 0
b = a[:]
for i in range(n):
    c = 1
    while b[i] % 2 == 0:
        c *= 2
        b[i] //= 2
    if c > r:
        r = c
for i in range(n):
    if a[i] % r == 0:
        k += 1
print(r, k)









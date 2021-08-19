n = int(input())
a = list(map(int, input().split()))
c = [0] * 8
for i in range(n):
    c[a[i]] += 1
x = min(c[1], c[2], c[4])
c[1] -= x
c[2] -= x
c[4] -= x
y = min(c[1], c[2], c[6])
c[1] -= y
c[2] -= y
c[6] -= y
z = min(c[1], c[3], c[6])
if 3 * (x + y + z) != n:
    print(-1)
else:
    for i in range(x):
        print(1, 2, 4)
    for i in range(y):
        print(1, 2, 6)
    for i in range(z):
        print(1, 3, 6)

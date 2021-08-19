(n, m) = list(map(int, input().split()))
u = list(map(int, input().split()))
a = list(map(int, input().split()))
u1 = 0
u2 = 0
for i in range(n):
    if u[i] % 2 == 0:
        u1 += 1
    else:
        u2 += 1
a1 = 0
a2 = 0
for i in range(m):
    if a[i] % 2 == 0:
        a1 += 1
    else:
        a2 += 1
print(min(u1, a2) + min(u2, a1))

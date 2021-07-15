n = int(input())
m = int(input())
u = []
for i in range(n):
    u.append(int(input()))
k = max(u)
a1 = k + m
for i in range(n):
    m -= k - u[i]
if m > 0:
    k += m // n
    if m % n != 0:
        k += 1
print(k, a1)


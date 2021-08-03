n = int(input())
m = int(input())
a = [0] * n
for i in range(n):
    a[i] = int(input())
a.sort(reverse=True)
k = 0
z = 0
while z < m:
    z += a[k]
    k += 1
print(k)

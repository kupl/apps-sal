n = int(input())
a = input().split()
for i in range(n):
    a[i] = int(a[i])
a = sorted(a)
m = int(input())
b = input().split()
for i in range(m):
    b[i] = int(b[i])
b = sorted(b)
pos1 = 0
pos2 = 0
k = 0
while pos1 < n and pos2 < m:
    if abs(a[pos1] - b[pos2]) <= 1:
        k += 1
        pos1 += 1
        pos2 += 1
    elif a[pos1] > b[pos2]:
        pos2 += 1
    else:
        pos1 += 1
print(k)

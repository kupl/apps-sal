(n, k) = map(int, input().split())
a = input().split()
for i in range(n):
    a[i] = int(a[i])
a.sort()
b = []
count = 0
for i in range(n):
    if i == 0:
        count += 1
        if i == n - 1:
            b.append([a[i], count])
    elif a[i] == a[i - 1]:
        count += 1
        if i == n - 1:
            b.append([a[i], count])
    else:
        b.append([a[i - 1], count])
        count = 1
        if i == n - 1:
            b.append([a[i], count])
while k:
    if len(b) == 1:
        break
    if b[0][1] < b[len(b) - 1][1]:
        if k >= (b[1][0] - b[0][0]) * b[0][1]:
            b[1][1] += b[0][1]
            k -= (b[1][0] - b[0][0]) * b[0][1]
            b.pop(0)
        else:
            b[0][0] += k // b[0][1]
            k = 0
    elif k >= (b[len(b) - 1][0] - b[len(b) - 2][0]) * b[len(b) - 1][1]:
        b[len(b) - 2][1] += b[len(b) - 1][1]
        k -= (b[len(b) - 1][0] - b[len(b) - 2][0]) * b[len(b) - 1][1]
        b.pop(len(b) - 1)
    else:
        b[len(b) - 1][0] -= k // b[len(b) - 1][1]
        k = 0
print(b[len(b) - 1][0] - b[0][0])

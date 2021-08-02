n = int(input())
a = []
for i in range(n):
    x, y = list(map(int, input().split()))
    a.append([x, 1])
    a.append([y, 0])
a.sort()
c = 0
m = 0
y = 0
for i in range(len(a)):
    if a[i][1] == 1:
        c += 1
    else:
        c -= 1
    if m < c:
        m = c
        y = a[i][0]
print(y, m)

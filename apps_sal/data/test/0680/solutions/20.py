(x1, y1) = list(map(int, input().split()))
(x2, y2) = list(map(int, input().split()))
(x3, y3) = list(map(int, input().split()))
k = max(y1, y2, y3) + 1 - min(y1, y2, y3) + max(x1, x2, x3) - min(x1, x2, x3)
m = [0, y1, y2, y3]
m.sort()
z = [0, x1, x2, x3]
z.sort()
print(k)
for i in range(z[1], z[3] + 1):
    print(str(i) + ' ' + str(m[2]))
for i in range(m[2] + 1, m[3] + 1):
    if m[3] == y3:
        print(str(x3) + ' ' + str(i))
    if m[3] == y2:
        print(str(x2) + ' ' + str(i))
    if m[3] == y1:
        print(str(x1) + ' ' + str(i))
for i in range(m[1], m[2]):
    if m[1] == y3:
        print(str(x3) + ' ' + str(i))
    if m[1] == y2:
        print(str(x2) + ' ' + str(i))
    if m[1] == y1:
        print(str(x1) + ' ' + str(i))

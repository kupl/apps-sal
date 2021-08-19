(x1, y1) = map(int, input().split())
(x2, y2) = map(int, input().split())
(x3, y3) = map(int, input().split())
mas = [[y1, x1], [y2, x2], [y3, x3]]
mas.sort()
for i in range(3):
    mas[i] = mas[i][::-1]
a = 0
ans = []
for i in range(mas[0][1], mas[1][1]):
    a += 1
    ans.append([mas[0][0], i])
for i in range(mas[2][1], mas[1][1], -1):
    a += 1
    ans.append([mas[2][0], i])
yy = mas[1][1]
mas.sort()
for i in range(mas[0][0], mas[2][0] + 1):
    a += 1
    ans.append([i, yy])
print(a)
for i in range(a):
    print(*ans[i])

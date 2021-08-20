(x1, y1) = list(map(int, input().split()))
(x2, y2) = list(map(int, input().split()))
x2 -= x1
y2 -= y1
x1 = 0
y1 = 0
n = int(input())
a = list(input())
r = [0, 0]
flag = True
for i in range(n):
    if a[i] == 'U':
        r[1] += 1
    if a[i] == 'D':
        r[1] -= 1
    if a[i] == 'L':
        r[0] -= 1
    if a[i] == 'R':
        r[0] += 1
left = 0
right = 90000000000
for i in range(2 * 10 ** 10):
    r1 = r[:]
    r1[0] *= (left + right) // 2
    r1[1] *= (left + right) // 2
    if abs(r1[0] - x2) + abs(r1[1] - y2) <= (left + right) // 2 * n:
        right = (left + right) // 2
    else:
        left = (left + right) // 2
    if right == 90000000000 and left == 90000000000 - 1:
        flag = False
    if left + 1 == right:
        break
rl = r[:]
rl[0] *= left
rl[1] *= left
if flag:
    for i in range(n):
        if a[i] == 'U':
            rl[1] += 1
        if a[i] == 'D':
            rl[1] -= 1
        if a[i] == 'L':
            rl[0] -= 1
        if a[i] == 'R':
            rl[0] += 1
        if abs(rl[0] - x2) + abs(rl[1] - y2) <= left * n + i + 1:
            print(left * n + i + 1)
            break
else:
    print(-1)

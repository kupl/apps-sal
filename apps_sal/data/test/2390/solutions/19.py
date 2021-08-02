N, C = map(int, input().split())
xv = [list(map(int, input().split())) for i in range(N)]

A1 = [0, 0]
X1 = [0]
A2 = [0, 0]
X2 = [0]
for x, v in xv:
    A1[-1] += v - x
    A1.append(A1[-1] + x)
    X1.append(x)
A1.pop()

xv = xv[::-1]
for x, v in xv:
    A2[-1] += v - (C - x)
    A2.append(A2[-1] + (C - x))
    X2.append(C - x)
A2.pop()

max_1 = []
max_2 = []
now = -1
for i, a in enumerate(A1):
    if a > now:
        max_1.append(i)
        now = a
    else:
        max_1.append(max_1[-1])

now = -1
for i, a in enumerate(A2):
    if a > now:
        max_2.append(i)
        now = a
    else:
        max_2.append(max_2[-1])

ans = 0
for i, a in enumerate(A1):
    idx = max_2[-i - 1]
    calory = max(a, a + A2[idx] - X1[i])
    ans = max(ans, calory)

for i, a in enumerate(A2):
    idx = max_1[-i - 1]
    calory = max(a, a + A1[idx] - X2[i])
    ans = max(ans, calory)

print(ans)

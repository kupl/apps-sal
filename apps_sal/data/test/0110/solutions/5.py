n = int(input())
a = []
for i in map(int, input().split()):
    if abs(-i - 1) > abs(i):
        a.append(-i - 1)
    else:
        a.append(i)

c = 0
for i in a:
    if i < 0:
        c += 1
if c % 2:
    me = 0
    for i in range(len(a)):
        if a[i] < a[me]:
            me = i
    a[me] = -a[me] - 1
print(*a)

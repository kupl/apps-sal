n = int(input())
a = list(map(int, input().split(' ')))
l = []
l.append(1)
s = []
s.append(a[0])
for i in range(1, n):
    if a[0] >= a[i] * 2:
        l.append(i + 1)
        s.append(a[i])
if sum(s) > sum(a) // 2:
    print(len(l))
    print(*l)
else:
    print(0)

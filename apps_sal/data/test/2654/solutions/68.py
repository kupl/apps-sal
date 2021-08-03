def med(l):
    t = len(l)
    if t % 2:
        return l[t // 2]
    else:
        return (l[t // 2] + l[t // 2 - 1]) / 2


n = int(input())
a = []
b = []
for i in range(n):
    x, y = list(map(int, input().split()))
    a += [x]
    b += [y]
a.sort()
b.sort()

if n % 2 == 0:
    print((int((med(b) - med(a)) * 2) + 1))
else:
    print((med(b) - med(a) + 1))

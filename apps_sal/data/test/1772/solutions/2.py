n = int(input())
a = list(map(int, input().split()))
b = 0
c = 0
for i in a:
    if i % 2 == 0:
        b += 1
    else:
        c += 1
d = min(b, c)
b -= d
c -= d
if c <= 0:
    print(d)
else:
    f = c // 3
    d += f
    print(d)

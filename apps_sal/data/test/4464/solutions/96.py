a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)
d = 0
for i in range(1000):
    if a * i % b == c:
        d = d + 1
if d == 0:
    print("NO")
else:
    print("YES")

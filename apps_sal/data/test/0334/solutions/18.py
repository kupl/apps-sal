(a, b) = map(int, input().split())
(c, d) = map(int, input().split())
if b > d:
    (b, d) = (d, b)
    (a, c) = (c, a)
d -= b
for i in range(1000000):
    if (c * i + d) % a == 0:
        print(i * c + d + b)
        break
else:
    print(-1)

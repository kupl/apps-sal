(a, b) = map(int, input().split())
c = b - a
d = 0
for i in range(c):
    d += i
print(d - a)

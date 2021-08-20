(a, b) = map(int, input().split())
d = b - a
d -= 1
x = 0
for i in range(d):
    x += i + 1
print(x - a)

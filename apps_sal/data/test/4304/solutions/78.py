a, b = map(int, input().split())
x = 0
for i in range(b - a):
    x += i
print(x - a)

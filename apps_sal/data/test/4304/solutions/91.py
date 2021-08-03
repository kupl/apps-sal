a, b = map(int, input().split())
c = abs(b - a)
x = 0
for i in range(1, c + 1):
    x += i
print(x - b)

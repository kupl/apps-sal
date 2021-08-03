a, b = list(map(int, input().split()))
height = 0
for i in range(b - a):
    height += i + 1
print(height - b)

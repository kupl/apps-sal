a, b = 0, 0
n = int(input())
for i in range(n):
    x, y = input().split()
    if y == 'soft':
        a += 1
    else:
        b += 1

for i in range(1, 1000):
    n = i * i
    y = n // 2
    x = n - y
    if (a <= x and b <= y) or (a <= y and b <= x):
        print(i)
        break

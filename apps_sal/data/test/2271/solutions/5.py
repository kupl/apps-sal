n = int(input())
a = [0] * (n + 1)
for _ in range(n - 1):
    x, y = input().split(' ')
    x, y = [int(x), int(y)]
    a[x] += 1
    a[y] += 1
too = 0
for x in a:
    too += (x * (x - 1)) // 2
print(too)

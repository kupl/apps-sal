R, d = list(map(int, input().split(" ")))
n = int(input())

caught = 0

for i in range(n):

    x, y, r = list(map(int, input().split(" ")))

    if (R - d + r) * (R - d + r) <= x * x + y * y and x * x + y * y <= (R - r) * (R - r):

        caught += 1

print(caught)

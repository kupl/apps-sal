n = int(input())
l = []
for i in range(n):
    (x, y) = [int(j) for j in input().split()]
    l.append((x, y))


def loss(x, y):
    maxi = 0
    for (i, j) in l:
        maxi = max(maxi, (i - x) ** 2 + (j - y) ** 2)
    return maxi


def f(x):
    left = 0
    right = 1000
    num = 100
    for i in range(num):
        c1 = (2 * left + right) / 3
        c2 = (left + 2 * right) / 3
        if loss(x, c1) < loss(x, c2):
            right = c2
        else:
            left = c1
    return loss(x, left)


left = 0
right = 1000
num = 100
for i in range(num):
    c1 = (2 * left + right) / 3
    c2 = (left + 2 * right) / 3
    if f(c1) < f(c2):
        right = c2
    else:
        left = c1
ans = f(left) ** 0.5
print(ans)

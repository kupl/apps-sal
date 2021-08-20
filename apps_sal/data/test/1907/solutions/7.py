s = 0
t = [list(map(int, input().split())) for i in range(int(input()))]


def f(b):
    return a[2] < b[2] and (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2 <= (a[2] - b[2]) ** 2


for a in t:
    k = sum((f(b) for b in t))
    s += (-1, 1)[(k < 1) + k & 1] * a[2] ** 2
print(3.1415926536 * s)

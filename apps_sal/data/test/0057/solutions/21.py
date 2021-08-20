def f(a, b):
    return abs((a[0] - b[0]) * (a[1] - b[1]))


n = int(input())
x = [list(map(int, input().split())) for i in range(n)]
y = 0
for i in range(n):
    for j in range(i + 1, n):
        if not y:
            y = f(x[i], x[j])
print(y or -1)

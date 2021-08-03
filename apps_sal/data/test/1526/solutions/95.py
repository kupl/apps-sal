a = sorted(list(map(int, input().split())))
x = 0
i = (a[1] - a[0]) // 2
x += i
a[1] -= i * 2
a[2] -= i * 2
i = (a[2] - a[1])
a[2] -= i
x += i
print(x + sum(a) - a[0] * 3)

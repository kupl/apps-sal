R = lambda: list(map(int, input().split()))
n, = R()
a = R()
b = R()
s = 0
for i in range(n):
    if 2 * a[i] < b[i] or b[i] == 1:
        s -= 1
    else:
        x = b[i] // 2
        y = b[i] - x
        s += x * y
print(s)

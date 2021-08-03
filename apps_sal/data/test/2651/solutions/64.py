n, m = map(int, input().split())
x = list(map(int, input().split()))
y = list(map(int, input().split()))
width, height = 0, 0
a = -n - 1
for k in range(1, n + 1):
    width += x[k - 1] * (2 * k + a)
a = -m - 1
for k in range(1, m + 1):
    height += y[k - 1] * (2 * k + a)
width %= 1000000007
height %= 1000000007
print(width * height % 1000000007)

n, c = list(map(int, input().split()))
x = list(map(int, input().split()))
ma = 0
for i in range(0, n - 1):
    ma = max(ma, x[i] - x[i + 1] - c)
print(ma)

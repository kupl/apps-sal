n, m = map(int, input().split())
x = list(map(int, input().split()))
y = list(map(int, input().split()))
sx = 0
sy = 0
pr = 10**9 + 7
for i in range(1, n):
    sx += (x[i] - x[i - 1]) * (i * (n - i)) % pr
for i in range(1, m):
    sy += (y[i] - y[i - 1]) * (i * (m - i)) % pr
print(sx * sy % pr)

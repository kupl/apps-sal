n, k = map(int, input().split())

x, y = map(int, input().split())

kayf = x - max(0, y - k)

for i in range(1, n):
    x, y = map(int, input().split())
    da = x - max(0, y - k)
    if da > kayf:
        kayf = da

print(kayf)

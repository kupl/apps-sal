k, n = list(map(int, input().split()))
a = list(map(int, input().split()))

route = []
for i in range(n - 1):
    move = a[i + 1] - a[i]
    route.append(move)

route.append(k - a[-1] + a[0])

print((sum(route) - max(route)))

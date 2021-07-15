n, t = map(int, input().split())
res = [float('inf'), 0]
for i in range(1, n + 1):
    s, d = map(int, input().split())
    x = max((t - s + d - 1) // d, 0)
    v = s + d * x
    # print(i, x, v)
    if res[0] > v:
        res = [v, i]
print(res[1])

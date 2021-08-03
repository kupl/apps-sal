n, m = map(int, input().split())
x = sorted(list(map(int, input().split())))
if n >= m:
    print(0)
else:
    x_dif = sorted([x[i] - x[i - 1] for i in range(1, m)], reverse=True)
    print(x[-1] - x[0] - sum(x_dif[:n - 1]))

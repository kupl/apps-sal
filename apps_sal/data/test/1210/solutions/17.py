def read():
    return list(map(int, input().split()))


def f(x):
    return (x[1] // p - (x[0] - 1) // p) / (x[1] - x[0] + 1)


(n, p) = read()
a = [f(tuple(read())) for i in range(n)]
ans = sum((1 - (1 - a[i]) * (1 - a[i - 1]) for i in range(n))) * 2000
print(ans)

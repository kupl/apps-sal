d = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]


def read():
    return list(map(int, input().split()))


def f(x):
    return sum((d[int(i)] for i in str(x)))


(a, b) = read()
p = [0] * (b + 1)
for i in range(1, b + 1):
    p[i] = p[i - 1] + f(i)
cnt = p[b] - p[a - 1]
print(cnt)

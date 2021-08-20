def f(k, c):
    e = s = 0
    for i in range(n):
        if (i - c) % k != 0:
            if a[i] == 1:
                e += 1
            else:
                s += 1
    return abs(e - s)


def read():
    return map(int, input().split())


(n, k) = read()
a = list(read())
mx = 0
for c in range(0, k):
    mx = max(mx, f(k, c))
print(mx)

def read():
    return map(int, input().split())


(n, k, p) = read()
A = sorted(read())
B = sorted(read())
res = 1e+18


def fun(x, y):
    return abs(x - y) + abs(y - p)


for i in range(k - n + 1):
    now = 0
    for j in range(n):
        c = fun(A[j], B[i + j])
        if c > now:
            now = c
    if now < res:
        res = now
print(res)
'\nInput:\n2 4 50\n20 100\n60 10 40 80\nOutput:\n50\n\n'

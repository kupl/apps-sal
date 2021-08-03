from sys import stdin, stdout


def mult(x, y):
    z = [0] * 128
    for i in range(128):
        for j in range(128):
            z[i ^ j] += x[i] * y[j]
    return z


n, x = map(int, stdin.readline().split())
a = list(map(float, stdin.readline().split()))
for _ in range(x, 128):
    a.append(0)
ans = [0] * 128
ans[0] = 1
while n > 0:
    if n % 2 == 1:
        ans = mult(ans, a)
    a = mult(a, a)
    n //= 2
stdout.write(str(1 - ans[0]))

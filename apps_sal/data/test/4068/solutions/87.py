def input2():
    return map(int, input().split())


def Fib(n):
    (a, b) = (0, 1)
    if n == 1:
        return a
    elif n == 2:
        return b
    else:
        for i in range(n - 2):
            (a, b) = (b, a + b)
        return b


(n, m) = input2()
A = [int(input()) for _ in range(m)]
INF = 1000000007
start = 0
ans = 1
for a in A:
    tmp = a - start
    if tmp > 1:
        fib = Fib(tmp + 1)
        ans *= fib
        ans %= INF
    elif tmp == 0:
        ans = 0
        break
    start = a + 1
if n - start > 1:
    ans *= Fib(n - start + 2)
    ans %= INF
print(ans)

def f(n):
    res = 1
    for i in range(2, n + 1):
        res = res * i
    return res


n = int(input())

if n == 2:
    print(1)
elif n == 4:
    print(3)
else:
    ans = f(n) // (2 * n * n)
    print(ans * 4)

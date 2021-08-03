def read(): return tuple(map(int, input().split()))


n, a, b, c = read()[0], read()[0], read()[0], read()[0]
n -= 1
if n == 0:
    print(0)
elif n == 1:
    print(min(a, b))
else:
    print(min(a + c * (n - 1), b + c * (n - 1), b * n, a * n))

n, a, b = list(map(int, input().split(" ")))
x = (a + 100 * n + b) % n
if x == 0:
    print(n)
else:
    print(x)

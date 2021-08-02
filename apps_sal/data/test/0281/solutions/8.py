a, b = list(map(int, input().split()))
if b - a > 12:
    print(0)
else:
    res = 1
    for i in range(a + 1, b + 1):
        res *= i
    print(res % 10)

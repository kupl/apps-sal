n = int(input())
if n <= 2:
    print(1)
elif n == 3:
    print(2)
else:
    s = 0
    a = int((2 * (n + 1)) ** 0.5)

    def l(x):
        return x * (x + 1) // 2
    for i in range(a, n):
        if l(i) > n + 1:
            print(n - i + 2)
            break

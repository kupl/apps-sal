(n, a, b, c) = (int(i) for i in input().split())
if n % 4 == 0:
    print(0)
else:
    ans = 10 ** 11
    for i in range(5):
        for j in range(5):
            for k in range(5):
                if (n + i * 1 + j * 2 + k * 3) % 4 == 0:
                    ans = min(ans, i * a + b * j + c * k)
    print(ans)

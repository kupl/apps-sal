(n, a, b) = list(map(int, input().split()))
for i in range(n // a + 1):
    if (n - i * a) % b == 0:
        res = []
        for j in range(i):
            t = [j * a + k for k in range(1, a + 1)]
            res += t[1:] + [t[0]]
        for j in range((n - i * a) // b):
            t = [i * a + j * b + k for k in range(1, b + 1)]
            res += t[1:] + [t[0]]
        print(*res)
        break
else:
    print(-1)

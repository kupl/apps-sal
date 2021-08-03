q = int(input())
for _ in range(q):
    n, a, b = list(map(int, input().split()))
    res = 0
    if n % 2 == 1:
        res += a
    res += (n // 2) * min(2 * a, b)
    print(res)

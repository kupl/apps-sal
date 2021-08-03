q = int(input())
for _ in range(q):
    n, a, b = list(map(int, input().split()))
    if 2 * a <= b:
        print(n * a)
    else:
        if n % 2:
            print(a + n // 2 * b)
        else:
            print(n // 2 * b)

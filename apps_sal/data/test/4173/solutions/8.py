q = int(input())
for x in range(q):
    (n, a, b) = list(map(int, input().split()))
    if a <= b // 2:
        print(n * a)
    else:
        print(b * (n // 2) + a * (n % 2))

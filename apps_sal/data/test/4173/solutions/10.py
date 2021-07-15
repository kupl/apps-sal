q = int(input())
for _ in range(q):
    n, a, b = (int(t) for t in input().split(' '))
    print(min(n * a, (n // 2) * b + (n % 2) * a))


q = int(input())
for i in range(q):
    (n, a, b) = map(int, input().split())
    print(min(n // 2 * b + n % 2 * a, n * a))

q = int(input())
for i in range(q):
    n, a, b = list(map(int, input().split()))
    num = 2 * a
    print(n // 2 * min(num, b) + n % 2 * a)

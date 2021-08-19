q = int(input())
for i in range(q):
    (n, x, a, b) = list(map(int, input().split()))
    print(min(abs(a - b) + x, n - 1))

t = int(input())
for _ in range(t):
    (x, y, n) = map(int, input().split())
    k = y
    k += (n - y) // x * x
    print(k)

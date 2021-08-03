t = int(input())
for i in range(t):
    n, m, a, b = list(map(int, input().split()))
    print(min(abs(a - b) + m, n - 1))

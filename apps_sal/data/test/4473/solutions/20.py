t = int(input())
for i in range(t):
    a, b, k = list(map(int, input().split()))
    print((k + 1) // 2 * a - (k // 2) * b)

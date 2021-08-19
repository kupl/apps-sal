t = int(input())
for i in range(t):
    (x, y, k) = list(map(int, input().split()))
    a = (y + 1) * k - 1
    print((a - 1) // (x - 1) + 1 + k)

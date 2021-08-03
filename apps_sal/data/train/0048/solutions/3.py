q = int(input())
for t in range(q):
    x, y, k = list(map(int, input().split()))
    a = ((y + 1) * k - 1 + x - 1 - 1) // (x - 1)
    b = k
    print(a + b)

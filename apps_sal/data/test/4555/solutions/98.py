a, b, k = list(map(int, input().split()))
if b - a + 1 < 2 * k:
    for i in range(a, b + 1):
        print(i)
else:
    for i in range(k):
        print((a + i))
    for j in range(k):
        print((b + j - k + 1))

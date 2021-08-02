a, b, k = map(int, input().split())
if b - a + 1 > k * 2:
    for i in range(a, a + k):
        print(i)
    for j in range(b - k + 1, b + 1):
        print(j)
else:
    for h in range(a, b + 1):
        print(h)

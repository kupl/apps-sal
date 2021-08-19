(a, b, k) = map(int, input().split())
if b - a >= k * 2 - 1:
    for i in range(k):
        print(a + i)
    for i in range(k):
        print(b + 1 - (k - i))
else:
    for j in range(a, b + 1):
        print(j)

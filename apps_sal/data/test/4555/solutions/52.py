a, b, k = list(map(int, input().split()))

for i in range(k):
    x = a + i
    if x <= b:
        print(a + i)

for i in range(k):
    x = b - k + i + 1
    if x <= a + k - 1 or x < a:
        pass
    else:
        print(x)

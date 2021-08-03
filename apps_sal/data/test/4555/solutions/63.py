a, b, k = map(int, input().split())

if b - a + 1 <= k * 2:
    for i in range(a, b + 1):
        print(i)

else:
    for j in range(a, a + k):
        print(j)

    for p in range(b - k + 1, b + 1):
        print(p)

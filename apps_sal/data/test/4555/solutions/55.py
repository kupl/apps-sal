a, b, k = map(int, input().split())
for i in range(a, min(b + 1, a + k)):
    print(i)
for j in range(max(b - k, a + k - 1), b):
    print(j + 1)

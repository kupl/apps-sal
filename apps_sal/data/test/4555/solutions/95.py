(a, b, k) = list(map(int, input().split()))
for i in range(k):
    if a + i > b:
        break
    print(a + i)
start = max(a + k, b - k + 1)
for i in range(start, b + 1):
    print(i)

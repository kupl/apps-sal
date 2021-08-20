(a, b, k) = map(int, input().split())
for i in range(a, a + k):
    if b < i:
        break
    print(i)
for i in range(max(a + k, b - k + 1), b + 1):
    if i < a:
        continue
    print(i)

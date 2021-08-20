(a, b, k) = map(int, input().split())
x = list()
for i in range(k):
    if a + i <= b:
        print(a + i)
        x.append(a + i)
for j in range(k):
    f = b - k + j + 1
    if a <= f and f <= b and (f not in x):
        print(f)

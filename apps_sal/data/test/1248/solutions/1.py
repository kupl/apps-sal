a, b, c = list(map(int, input().split()))

for i in range(100):
    a = min(a, b + c)
    b = min(b, a + c)
    c = min(c, a + b)

print(a + b + c)

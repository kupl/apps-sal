n, a, b = list(map(int, input().split()))
for i in range(abs(b)):
    a += (1 if b > 0 else -1)
    if a == 0:
        a = n
    if a == n + 1:
        a = 1
print(a)

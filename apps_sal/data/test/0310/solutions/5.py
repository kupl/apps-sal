



n, k = list(map(int, input().split()))

a, b, c = 0, k, 0

while a < b:
    c = (a + b) // 2
    if c * n < k:
        a = c + 1
    else:
        b = c

print(a)


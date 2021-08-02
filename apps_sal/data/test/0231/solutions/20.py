n, a = list(map(int, input().split()))

if a % 2 == 0:
    a = n // 2 - a // 2
else:
    a = (a - 1) // 2

print(a + 1)

(a, p) = map(int, input().split())
m = a * 3 + p
if m % 2 == 0:
    print(m // 2)
else:
    print((m - 1) // 2)

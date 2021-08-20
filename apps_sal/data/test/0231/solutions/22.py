(n, a) = list(map(int, input().split()))
if a % 2 == 1:
    print((a + 1) // 2)
else:
    print((n - a + 2) // 2)

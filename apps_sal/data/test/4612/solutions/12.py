(a, b) = map(int, input().split())
if a % 2 == 0 and b % 2 == 0 or (a % 2 == 1 and b % 2 == 1):
    print((a + b) // 2)
else:
    print((a + b) // 2 + 1)

t = int(input())
for test in range(t):
    x = int(input())
    a = len(str(x))
    print((x % 10 - 1) * 10 + a * (a + 1) // 2)

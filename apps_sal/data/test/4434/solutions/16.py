t = int(input())
for _ in range(t):
    n = int(input())
    s = 0
    for i in range(n // 2):
        s = s + 8 * (i + 1) * (i + 1)
    print(s)

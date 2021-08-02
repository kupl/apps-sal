X = int(input())
now = 100
for i in range(10000):
    now *= 101
    now //= 100
    if now >= X:
        print(i + 1)
        break

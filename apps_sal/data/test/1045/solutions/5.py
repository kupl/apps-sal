n = int(input())

s = 0
for i in range(10000):
    s += i * (i + 1) // 2
    if s > n:
        print(i - 1)
        return


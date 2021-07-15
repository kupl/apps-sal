n, k = map(int, input().split())

current = 0
for i in range(1, n + 1):
    current += 5 * i
    if 60 * 4 - current - k < 0:
        print(i - 1)
        return
print(n)

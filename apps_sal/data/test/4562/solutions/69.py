n = int(input())
for i in range(1, 10 ** 5):
    p = i ** 2
    if p > n:
        print((i - 1) ** 2)
        break

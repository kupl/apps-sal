n = int(input())
c = 0
for i in range(1, 8):
    if 2 ** i > n:
        print(2 ** (i - 1))
        break

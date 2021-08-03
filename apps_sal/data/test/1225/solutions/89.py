H = int(input())
for i in range(0, 10**20 + 1):
    if 2**i <= H < 2 ** (i + 1):
        break
print(2 ** (i + 1) - 1)

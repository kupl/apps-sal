k = int(input())
ch = 0
i = 0
r = 1
while k > r - 1:
    r += 9 * (i + 1) * 10 ** i
    i += 1
r -= 9 * i * 10 ** (i - 1)
print(str((k - r) // i + 10 ** (i - 1))[(k - r) % i])

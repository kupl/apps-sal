l = int(input())
n = len(bin(l)) - 3
tmp = 2 ** n
print((n + 1, 2 * n + bin(l)[3:].count('1')))
for i in range(n):
    print((i + 1, i + 2, 0))
    print((i + 1, i + 2, 2 ** i))
    if l & 1 << i:
        print((i + 1, n + 1, tmp))
        tmp += 2 ** i

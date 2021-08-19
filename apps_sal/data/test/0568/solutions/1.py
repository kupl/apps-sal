n = int(input())
p = 3 ** (3 * n)
p -= 7 ** n
print(p % (10 ** 9 + 7))

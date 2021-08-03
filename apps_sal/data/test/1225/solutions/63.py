hp = int(input())
n = 0

while hp:
    hp //= 2
    n += 1

print(2**n - 1)

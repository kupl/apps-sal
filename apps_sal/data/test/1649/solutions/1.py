from itertools import product

cookie = list(map(int, input().split()))

for bit in product([0, 1], repeat=4):
    eat = 0
    not_eat = 0
    for i, b in enumerate(bit):
        if b == 0:
            eat += cookie[i]
        else:
            not_eat += cookie[i]
    if eat == not_eat:
        print("Yes")
        return
print("No")

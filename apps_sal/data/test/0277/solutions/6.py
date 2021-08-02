n, a, b = list(map(int, input().split()))

a -= 1
b -= 1

n_round = 0
while n > 2:
    n_round += 1
    a //= 2
    b //= 2
    n //= 2
    if a == b:
        break
else:
    print('Final!')
    return

print(n_round)

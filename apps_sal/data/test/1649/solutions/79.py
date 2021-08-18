A = list(map(int, input().split()))
yes = False
for bitset in range(1, 2 ** 4):
    eat_sum = 0
    left_sum = 0
    for j in range(4):
        if ((bitset >> j) & 1) == 1:
            eat_sum += A[j]
        else:
            left_sum += A[j]

    if eat_sum == left_sum:
        yes = True
        break

if yes:
    print("Yes")
else:
    print("No")

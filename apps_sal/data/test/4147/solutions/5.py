from itertools import product
(N, A, B, C) = list(map(int, input().split(' ')))
L = [int(input()) for _ in range(N)]
ans = 10 ** 9
for groups in product(list(range(4)), repeat=N):
    length_a = 0
    length_b = 0
    length_c = 0
    cost_a = -10
    cost_b = -10
    cost_c = -10
    for (group, length) in zip(groups, L):
        if group == 1:
            length_a += length
            cost_a += 10
        elif group == 2:
            length_b += length
            cost_b += 10
        elif group == 3:
            length_c += length
            cost_c += 10
    if 0 in {length_a, length_b, length_c}:
        continue
    ans = min(ans, sum([abs(A - length_a), abs(B - length_b), abs(C - length_c), cost_a, cost_b, cost_c]))
print(ans)

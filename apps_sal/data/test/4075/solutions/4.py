from itertools import product


N, M = list(map(int, input().split()))
bulbs = [list([int(x) - 1 for x in input().split()]) for _ in range(M)]
P = list(map(int, input().split()))

ans = 0
for x in product([0, 1], repeat=N):
    is_on = [0] * M
    for i in range(M):
        k, *switches = bulbs[i]
        cnt = sum(x[s] for s in switches)
        if cnt % 2 == P[i]:
            is_on[i] = 1
    if all(is_on):
        ans += 1
print(ans)

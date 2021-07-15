import itertools as it

N, M, X = map(int, input().split())
book = [[int(_) for _ in input().split()] for i in range(N)]

combs = it.product([0, 1], repeat=N)
prices = []
for comb in combs:
    # print(comb)
    bag = [0] * (M+1)
    for i in range(N):
        if comb[i] == 0:
            continue
        else:
            for j in range(M+1):
                bag[j] += book[i][j]

    if min(bag[1:]) < X:
        continue
    else:
        prices.append(bag[0])

if len(prices) == 0:
    print(-1)
else:
    print(min(prices))

(N, C) = map(int, input().split())
Dmat = []
for i in range(C):
    array = list(map(int, input().split()))
    Dmat.append(array)
grid_list = [{}, {}, {}]
for i in range(N):
    array = list(map(int, input().split()))
    for j in range(N):
        c = array[j] - 1
        mod = (i + j) % 3
        if c in grid_list[mod]:
            grid_list[mod][c] += 1
        else:
            grid_list[mod][c] = 1
min_cost = 10 ** 9
for i in range(C):
    for j in range(C):
        if i == j:
            continue
        for k in range(C):
            if i == k or j == k:
                continue
            cost = 0
            for (c, num) in grid_list[0].items():
                cost += Dmat[c][i] * num
            for (c, num) in grid_list[1].items():
                cost += Dmat[c][j] * num
            for (c, num) in grid_list[2].items():
                cost += Dmat[c][k] * num
            if cost < min_cost:
                min_cost = cost
print(min_cost)

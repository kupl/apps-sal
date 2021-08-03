import itertools

N, M, Q = map(int, input().split())
X = [list(map(int, input().split())) for i in range(Q)]

L = list(itertools.combinations_with_replacement(range(1, M + 1), N))
p_list = []

for l in L:
    point = 0
    for x in X:
        if l[x[1] - 1] - l[x[0] - 1] == x[2]:
            point += x[3]

    p_list.append(point)

# print(X)
# print(L)
# print(p_list)
print(max(p_list))

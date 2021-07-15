import itertools

N, C = list(map(int, input().split()))
MAX = 10 ** 5 + 1
table = [[0] * MAX for _ in range(C)]

for _ in range(N):
    s, t, c = list(map(int, input().split()))
    c -= 1
    table[c][s] += 1
    table[c][t] -= 1

for c in range(C):
    for x in range(MAX - 1):
        if table[c][x + 1] == 1:
            table[c][x + 1] = 0
            table[c][x] += 1

table_sum = [sum(table[c][i] for c in range(C)) for i in range(MAX)]
print((max(itertools.accumulate(table_sum))))


(N, T) = map(int, input().split())
c = []
min_cost = 10000
for i in range(N):
    (c, t) = map(int, input().split())
    if t <= T and c < min_cost:
        min_cost = c
print(min_cost) if min_cost <= 1000 else print('TLE')

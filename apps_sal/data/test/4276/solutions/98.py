(N, T) = list(map(int, input().split()))
cost = 'TLE'
for i in range(N):
    (c, t) = list(map(int, input().split()))
    if t <= T:
        if cost == 'TLE':
            cost = c
        elif cost > c:
            cost = c
print(cost)

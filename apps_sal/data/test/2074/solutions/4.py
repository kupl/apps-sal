
"""

"""

n, m = [int(i) for i in input().split()]

city = []

for i in range(n):
    city.append([int(i) for i in input().split()])

ma = 0

for i in range(n):
    ml = 1e10

    for j in range(m):
        ml = min(ml, city[i][j])

    ma = max(ma, ml)

print(ma)

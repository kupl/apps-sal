
n = int(input())
park = input().split(' ')
park = [int(i) for i in park]
park.insert(0, 0)
lights = [0 for i in range(2 ** (n + 1) - 1)]
res = 0
for k in range(n, 0, -1):
    for i, j in tuple(enumerate(park))[(2 ** k) - 1:2 ** (k + 1) - 1:2]:
        res += abs(j + lights[i] - park[i + 1] - lights[i + 1])
        lights[i // 2] = max(j + lights[i], park[i + 1] + lights[i + 1])
print(res)

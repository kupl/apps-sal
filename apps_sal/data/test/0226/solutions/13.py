n = int(input())
pies = [int(x) for x in input().split()]

d = {}
d[0] = pies[-1]

for i in range(1, n):
    d[i] = max(sum(pies[-1 - i:]) - d[i - 1], d[i - 1])

s = sum(pies)

res = d[n - 1]

print(s - res, res)

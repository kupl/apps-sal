n, m = [int(x) for x in input().split()]
d = [0] * n
inp = [int(x) - 1 for x in input().split()]
for i in range(m):
    d[inp[i]] += 1
print(min(d))

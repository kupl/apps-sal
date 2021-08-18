a = [int(x) for x in input().split()][1:]
a.sort()
res = 0
for i in range(7000000):
    res ^= i

print(' '.join([str(x) for x in a]))

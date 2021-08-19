n = int(input())
a = [int(x) for x in input().split()]
m = {i: 0 for i in range(1, n + 1)}
for (i, x) in enumerate(a):
    m[x] += 1
for x in range(1, n + 1):
    print(m[x])

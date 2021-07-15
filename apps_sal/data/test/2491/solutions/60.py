n, m = [int(i) for i in input().split()]
e = [[int(i) for i in input().split()] for i in range(m)]
v = [-(10 ** 9 * 2000)] * n

# Bellman-Ford
v[0] = 0
for i in range(n):
    tmp = v[-1]
    for a, b, cost in e:
        if v[a-1] + cost > v[b-1]:
            v[b-1] = v[a-1] + cost
    if tmp != v[-1] and i == n-1: break        
else:
    print((v[n-1]))
    return

print("inf")


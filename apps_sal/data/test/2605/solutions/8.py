n, k = [int(x) for x in input().split()]
c = [int(x) for x in input().split()]
capitals = set([int(x) - 1 for x in input().split()])

r = c[0] * c[-1]

for i in range(n-1):
    r += c[i] * c[i+1]

c_sum = sum(c)

for i in capitals:
    k = c_sum - c[i] - c[(i-1)%n]
    if (i+1)%n not in capitals:
        k -= c[(i+1)%n]
    r += c[i] * k
    c_sum -= c[i]

print(r)


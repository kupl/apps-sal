def cost(i, j=1):
    return abs(a[i] - a[i+j])

n = int(input())
a = [0] + [int(i) for i in input().split()] + [0]

c = sum([cost(i) for i in range(n+1)])
for i in range(1, n+1):
    print(c - cost(i-1) - cost(i) + cost(i-1, 2))

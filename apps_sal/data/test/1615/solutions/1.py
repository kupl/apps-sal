n, m = list(map(int, input().split()))
tot = sum([x[1] - x[0] + 1 for x in [[int(x) for x in input().split()] for i in range(n)]])
print((m - tot % m) % m)

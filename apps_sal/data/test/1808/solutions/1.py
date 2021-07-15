n, k, x = map(int, input().split())
print(sum([int(x) for x in input().split()][:n - k]) + k * x)

n, k, x = map(int, input().split())
k = min(k, n)
print(sum([int(s) for s in input().split()][:-k]) + k * x)

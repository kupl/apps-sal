n, k = map(int, input().split())
a = sorted([int(x) for x in input().split()])
print(sum(a[:k]))

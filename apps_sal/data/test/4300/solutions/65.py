import itertools as it
N = int(input())
d = list(map(int, input().split()))

k = list(it.combinations(d, 2))
n = [a * b for a, b in k]

print(sum(n))

import itertools
n = int(input())

a = list(map(int, input().split()))

pattern = itertools.combinations(a, 2)
total = 0
for i, j in pattern:
    total += i * j
print(total)

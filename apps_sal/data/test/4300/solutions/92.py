import itertools
N = int(input())
d = list(map(int, input().split()))
rec = 0
for tako in itertools.combinations(d, 2):
    rec += tako[0] * tako[1]
print(rec)

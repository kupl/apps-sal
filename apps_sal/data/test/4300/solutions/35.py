import itertools
total = 0
recovery = 0
n = int(input())
di = list(map(int, input().split()))
for x in itertools.combinations(di, 2):
    recovery = x[0] * x[1]
    total += recovery
print(total)

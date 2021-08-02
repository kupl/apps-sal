import itertools

N = int(input())
D = list(map(int, input().split()))

res = 0
for i, j in itertools.combinations(D, 2):
    res += i * j
print(res)

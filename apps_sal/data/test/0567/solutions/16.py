n = int(input())
d = list(map(int, input().split()))
res = 0
for x in d:
    res = max(res, min(x - 1, 1000000 - x))
print(res)

n = int(input())
a = [*map(int, input().split())]
b = [*map(int, input().split())]
d = {e: i for (i, e) in enumerate(a)}
res = 0
cur = float('inf')
for e in b[::-1]:
    if d[e] > cur:
        res += 1
    else:
        cur = d[e]
print(res)

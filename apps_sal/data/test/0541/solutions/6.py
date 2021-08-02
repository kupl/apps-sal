N, M = list(map(int, input().split()))
B = [tuple(map(int, input().split())) for _ in range(M)]
B.sort()
r = 0
res = 0
for a, b in B:
    if a >= r:
        res += 1
        r = b
    else:
        r = min(r, b)
print(res)

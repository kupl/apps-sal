n, d = list(map(int, input().strip().split()))
res = 0
cur = 0
for _ in range(d):
    if n == input().strip().count('1'):
        res = max(res, cur)
        cur = 0
    else:
        cur += 1
print(max(res, cur))


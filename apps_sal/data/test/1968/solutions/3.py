n, v = list(map(int, input().split()))
res = []
for i in range(n):
    k, *s = list(map(int, input().split()))
    if v > min(s):
        res.append(i + 1)
print(len(res))
print(' '.join(map(str, res)))

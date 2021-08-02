n, t = list(map(int, input().split()))
tn = list(map(int, input().split()))
res = t
for i in range(1, n):
    tmp = min(tn[i] - tn[i - 1], t)
    res += tmp

print(res)

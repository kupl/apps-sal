(n, k) = map(int, input().split())
seq = list(map(int, input().split()))
seq = sorted(seq)
res = -1
if k == 0:
    res = seq[0] - 1
    if res < 1:
        res = -1
elif k == n:
    res = seq[-1]
else:
    at_k = seq[k - 1]
    at_k1 = seq[k]
    if at_k == at_k1:
        res = -1
    else:
        res = at_k
print(res)

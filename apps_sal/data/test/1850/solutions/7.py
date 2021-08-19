(n, d) = [int(x) for x in input().split()]
sk = [int(x) for x in input().split()]
pk = [int(x) for x in input().split()]
maxm = sk[d - 1] + max(pk)
dip = 0
pkk = 1
for k in range(0, d):
    if sk[k] + pk[-pkk] <= maxm:
        dip += 1
        pkk += 1
print(d - dip + 1)

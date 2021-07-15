n, m = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]

res = 0
i, j = 0, 0
sa, sb = 0, 0
while i < n or j < m:
    if sa>sb:
        sb+=b[j]
        j+=1
    else:
        sa+=a[i]
        i+=1
    if sa == sb:
        res += 1
        sa = 0
        sb = 0

print(res)


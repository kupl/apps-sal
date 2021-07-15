n = int(input())

sn = str(n)
k = len(sn)


ans = 1
for i in sn:
    ans *= int(i)

for i in range(k-1):
    n -= (10 ** (i+1))
    n //= (10 ** (i+1))
    n *= (10 ** (i+1))
    n += (10 ** (i+1)) - 1
    if (n < 0):
        break
    sn = str(n)
    res = 1
    for i in sn:
        res *= int(i)
    ans = max(res, ans)
    #print(n)

print(ans)


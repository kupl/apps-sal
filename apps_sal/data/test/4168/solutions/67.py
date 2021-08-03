N = int(input())

res = []
sign = 1
while N:
    if N % 2 == 0:
        res.append(0)
    else:
        N -= sign
        res.append(1)
    N //= 2
    sign *= -1
if not res:
    res = [0]
print(*reversed(res), sep='')

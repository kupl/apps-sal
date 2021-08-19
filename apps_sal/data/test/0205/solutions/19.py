n, b = list(map(int, input().split()))
now = 1
p = []
isp = [1] * 1000001
for i in range(2, 10 ** 6 + 1):
    if isp[i]:
        p.append(i)
    for x in p:
        if x * i > 1000000:
            break
        isp[x * i] = 0
        if i < x or i % x == 0:
            break
# print(len(p))
de = []
for prime in p:
    count = 0
    while b % prime == 0:
        b //= prime
        count += 1
    if count:
        de.append((prime, count))
    if b < prime:
        break
if b != 1:
    de.append((b, 1))
# print(de)

ans = 10 ** 20
for pair in de:
    tmp = 1
    has = 0
    num, count = pair[0], pair[1]
    while tmp <= n:
        tmp *= num
        has += n // tmp
    ans = min(ans, has // count)
print(ans)

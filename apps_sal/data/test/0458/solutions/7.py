def sd(n):
    val = 0
    while n > 0:
        val += n % 10
        n //= 10
    return val


a, b, c = (int(x) for x in input().split())
l = []
for s in range(1, 82):
    cur = b * s ** a + c
    if cur > 0 and cur < 10 ** 9 and sd(cur) == s:
        l.append(cur)

l.sort()
print(len(l))
print(' '.join(str(x) for x in l))

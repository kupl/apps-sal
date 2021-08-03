l = int(input())
n = 0
while 2**n <= l:
    n += 1
p = []
for i in range(1, n):
    p.append((i, i + 1, 0))
    p.append((i, i + 1, 2**(i - 1)))
    if l // (2**(i - 1)) % 2 == 1:
        p.append((i, n, l // 2**i * 2**i))
m = len(p)
print((n, m))
for i in p:
    print((*i))

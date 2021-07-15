n = int(input())

cnt = 0
res = []

while n & (n + 1) and cnt < 40:
    if cnt % 2 == 0:
        b = bin(n)
        l = len(b) - 2
        i = bin(n)[2:].index('0')
        res.append(l - i)
        n ^= (1 << (l - i)) - 1
    else:
        n += 1
    cnt += 1

print(cnt)
if len(res) != 0:
    print(*res)


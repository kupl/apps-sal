def s(n):
    return n / sum(map(int, str(n)))


k = int(input())

x = 1
e = 0
i = 0

while i < k:

    tmp = (x + 1) * 10 ** e - 1
    nxt = (x + 2) * 10 ** e - 1

    if s(tmp) <= s(nxt):
        print(tmp)
        x += 1
        i += 1
    else:
        e += 1
        x = (x + 1) // 10

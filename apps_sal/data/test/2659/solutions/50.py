def s(n):
    return n / sum(map(int, str(n)))


k = int(input())
p = 1
e = 0
i = 0
while i < k:
    n = (p + 1) * 10**e - 1
    nxt = (p + 2) * 10**e - 1
    if s(n) <= s(nxt):
        print(n)
        p += 1
        i += 1
    else:
        e += 1
        p = (p + 1) // 10

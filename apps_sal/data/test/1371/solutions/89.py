S = int(input())
a = 0
if S < 3:
    print((0))
else:
    for i in range(S // 3):
        n = S - 3 * (i + 1) + i
        c = 1
        for k in range(i):
            c *= (n - k)
        for k in range(i):
            c //= (k + 1)
        a += c
    print((a % (10**9 + 7)))

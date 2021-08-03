t = int(input())
for _ in range(t):
    n = int(input())
    ct2, ct3 = 0, 0
    while n % 2 == 0:
        n /= 2
        ct2 += 1
    while n % 3 == 0:
        n /= 3
        ct3 += 1
    if n > 1 or ct2 > ct3:
        print(-1)
    else:
        print(ct3 + ct3 - ct2)

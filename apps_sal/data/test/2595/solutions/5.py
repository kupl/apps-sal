from math import log
t = int(input())
for _ in range(t):
    (a, b) = sorted(map(int, input().split()))
    if b % a != 0:
        print(-1)
        continue
    q = b // a
    ops = round(log(q, 2))
    if 2 ** ops != q:
        print(-1)
        continue
    print((ops + 2) // 3)

n = sorted([int(input()) for _ in range(int(input()))])
(r, a) = (sum(n), 0)
if r % 10 == 0:
    for i in n:
        if (r - i) % 10 != 0:
            a = max(a, r - i)
    print(a)
else:
    print(r)

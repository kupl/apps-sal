n = int(input())
a = list(map(int, input().split()))
s = sum(a)
if s % 2 == 0:
    print(s)
else:
    cmin = 10 ** 9 + 1
    for c in a:
        if c % 2 == 1 and c < cmin:
            cmin = c
    s -= cmin
    print(s)

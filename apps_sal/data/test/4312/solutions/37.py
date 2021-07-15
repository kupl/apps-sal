a, b, c, d = list(map(int, input().split()))

for i in range(220):
    if i % 2 == 0:
        c -= b
    else:
        a -= d

    if c <= 0:
        print('Yes')
        return
    elif a <= 0:
        print('No')
        return


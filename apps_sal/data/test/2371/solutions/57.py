n, z, w = list(map(int, input().split()))
card = list(map(int, input().split()))

if n == 1:
    print((abs(card[0] - w)))
else:
    print((max(abs(card[-2] - card[-1]), abs(card[-1] - w))))

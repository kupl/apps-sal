a, b, c, d = map(int, input().split())
flg = 0
for i in range(10**100):
    if(flg == 0):
        c -= b
        flg = 1
    else:
        a -= d
        flg = 0

    if(a <= 0 or c <= 0):
        print('Yes' if c <= 0 else 'No')
        break

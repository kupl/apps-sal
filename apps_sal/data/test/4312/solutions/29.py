a, b, c, d = list(map(int, input().split()))
count = 0
while True:
    c -= b
    if c <= 0:
        print('Yes')
        break
    a -= d
    if a <= 0:
        print('No')
        break


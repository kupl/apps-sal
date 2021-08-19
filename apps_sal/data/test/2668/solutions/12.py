(a, b, c) = list(map(int, input().split()))
c = (c - a) // b
if c % 2 == 0:
    print('Lucky Chef')
else:
    print('Unlucky Chef')

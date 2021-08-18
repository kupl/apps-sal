n, m = tuple(int(x) for x in input().split())
right = True
while n:
    if n % 2 == 1:
        print('
    else:
        if right:
            print('.' * (m - 1), '
            right=False
        else:
            print('
            right=True
    n -= 1

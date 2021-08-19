for _ in range(int(input())):
    (n, a, b, c, d) = map(int, input().split())
    (al, ar) = (n * (a - b), n * (a + b))
    (bl, br) = (c - d, c + d)
    if al <= bl <= ar or al <= br <= ar or bl <= al <= br or (bl <= ar <= br):
        print('Yes')
    else:
        print('No')

for _ in range(int(input())):
    D = input().split(':')
    if not D[0]:
        D = D[1:]
    if not D[-1]:
        D.pop()

    n = len(D)
    for i in range(n):
        D[i] = D[i].zfill(4) if D[i] else '0000:' * (8 - n) + '0000'

    print(':'.join(D))

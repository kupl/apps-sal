def main():
    n, c = [int(t) for t in input().split()]
    p = [int(t) for t in input().split()]
    t = [int(t) for t in input().split()]

    limak_score, x = 0, 0
    for pi, ti in zip(p, t):
        x += ti
        limak_score += max(0, pi - c * x)

    radewoosh_score, x = 0, 0
    for pi, ti in zip(reversed(p), reversed(t)):
        x += ti
        radewoosh_score += max(0, pi - c * x)

    if limak_score > radewoosh_score:
        print('Limak')
    elif radewoosh_score > limak_score:
        print('Radewoosh')
    else:
        print('Tie')


def __starting_point():
    main()

__starting_point()

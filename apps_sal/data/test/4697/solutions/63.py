(S, C) = [int(n) for n in input().split(' ')]
if 2 * S >= C:
    print(min([S, int(C / 2)]))
else:
    print(S + int((C - 2 * S) / 4))

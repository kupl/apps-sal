[s, p] = list(map(int, input().split()))


def search(s, p):
    for n in range(1, int(s / 2) + 1):
        if n * (s - n) == p:
            return True
        if n * (s - n) > p:
            return False
    return False


if search(s, p):
    print('Yes')
else:
    print('No')

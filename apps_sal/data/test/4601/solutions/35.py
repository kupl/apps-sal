def main():
    n, k = list(map(int, input().split()))
    h = [int(v) for v in input().split()]
    if k >= len(h):
        return 0
    monsters = sorted(h)
    monsters.reverse()
    return sum(monsters[k:])


def __starting_point():
    print((main()))


__starting_point()

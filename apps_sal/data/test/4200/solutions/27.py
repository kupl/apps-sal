def main():
    n, m = list(map(int, input().split()))
    a = [int(v) for v in input().split()]
    total = sum(a)
    variant = total * (1 / (4 * m))
    cnt = 0
    for i in a:
        if i >= variant:
            cnt += 1
    return "Yes" if cnt >= m else "No"


def __starting_point():
    print((main()))


__starting_point()

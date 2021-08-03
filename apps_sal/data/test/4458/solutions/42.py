def main():
    n = int(input())
    p = [int(v) for v in input().split()]
    ans = 1
    sofar = p[0]
    for i in range(1, len(p)):
        sofar = min(p[i - 1], sofar)
        if p[i] < sofar:
            ans += 1
    return ans


def __starting_point():
    print((main()))


__starting_point()

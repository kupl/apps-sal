
def solve():
    n = int(input())
    al = set([int(i) for i in input().split()])
    for i in range(1001):
        al = al - set([i * i])
    print(max(al))


def __starting_point():
    solve()


__starting_point()

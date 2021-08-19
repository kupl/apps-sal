def solve(a):
    for ea in map(enumerate, (a, a[::-1])):
        next(ea)
        for (i, ai) in ea:
            yield (ai // i)


def main():
    input()
    print(min(solve(tuple(map(int, input().split())))))


main()

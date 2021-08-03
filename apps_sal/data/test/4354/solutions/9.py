import itertools
url = "https://atcoder.jp//contests/abc057/tasks/abc057_a"


def main():
    n, m = list(map(int, input().split()))
    ab = [list(map(int, input().split())) for _ in range(n)]
    cd = [list(map(int, input().split())) for _ in range(m)]
    for i in range(len(ab)):
        dist = []
        for k in range(len(cd)):
            tmp = abs(ab[i][0] - cd[k][0]) + abs(ab[i][1] - cd[k][1])
            dist.append(tmp)
        print(dist.index(min(dist)) + 1)


def __starting_point():
    main()


__starting_point()

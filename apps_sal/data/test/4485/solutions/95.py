#!/usr/bin/env python3

def main():
    n, m = list(map(int, input().split()))
    ab = [list(map(int, input().split())) for i in range(m)]
    ans = "IMPOSSIBLE"
    list_1 = []
    list_n = []
    for i in range(m):
        if ab[i][0] == 1:
            list_1.append(ab[i][1])
        elif ab[i][1] == n:
            list_n.append(ab[i][0])
    if len(set(list_1) & set(list_n)) > 0:
        ans = "POSSIBLE"
    print(ans)


def __starting_point():
    main()

__starting_point()

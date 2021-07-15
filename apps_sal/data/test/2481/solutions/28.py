#!/usr/bin/env python3
def main():
    H, W = list(map(int, input().split()))
    max_num = 10
    c = [list(map(int, input().split())) for _ in range(max_num)]
    A = [list(map(int, input().split())) for _ in range(H)]

    for k in range(max_num):
        for i in range(max_num):
            for j in range(max_num):
                c[i][j] = min(c[i][j], c[i][k] + c[k][j])

    ans = 0
    for row in A:
        for a in row:
            if a == -1:
                continue
            ans += c[a][1]
    print(ans)


def __starting_point():
    main()

__starting_point()

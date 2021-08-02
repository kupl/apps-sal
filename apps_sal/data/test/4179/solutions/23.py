# -*-coding:utf-8-*-
import sys
input = sys.stdin.readline


def main():
    n, m, c = map(int, input().split())
    base_data = []
    source_codes = []
    base_data = list(map(int, input().split()))
    source_codes = [list(map(int, input().split())) for _ in range(n)]
    ans = 0
    cnt = 0

    for i in range(n):
        for j in range(m):
            ans += source_codes[i][j] * base_data[j]
        ans = ans + c
        if ans > 0:
            ans = 0
            cnt += 1
        else:
            ans = 0
            continue

    print(cnt)


def __starting_point():
    main()


__starting_point()

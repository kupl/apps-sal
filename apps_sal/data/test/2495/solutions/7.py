import sys
input = sys.stdin.readline


def main():
    N = int(input())
    A = list(map(int, input().split()))
    tmp_o = [0 for i in range(N + 1)]
    tmp_e = [0 for i in range(N + 1)]
    count_o = 0
    count_e = 0
    for i in range(N):
        tmp_o[i + 1] = tmp_o[i] + A[i]
        if i % 2 == 1 and tmp_o[i + 1] <= 0:
            count_o += 1 - tmp_o[i + 1]
            tmp_o[i + 1] = 1
        elif i % 2 == 0 and tmp_o[i + 1] >= 0:
            count_o += tmp_o[i + 1] + 1
            tmp_o[i + 1] = -1
        else:
            continue
    for i in range(N):
        tmp_e[i + 1] = tmp_e[i] + A[i]
        if i % 2 == 0 and tmp_e[i + 1] <= 0:
            count_e += 1 - tmp_e[i + 1]
            tmp_e[i + 1] = 1
        elif i % 2 == 1 and tmp_e[i + 1] >= 0:
            count_e += tmp_e[i + 1] + 1
            tmp_e[i + 1] = -1
        else:
            continue

    print(min(count_o, count_e))


def __starting_point():
    main()


__starting_point()

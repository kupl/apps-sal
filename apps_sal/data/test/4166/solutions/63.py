import sys

input = sys.stdin.readline


def main():
    ans = 0
    N, M = map(int, input().split())
    i = [''] * N
    for _ in range(M):
        s, c = input().split()
        if i[int(s) - 1] != '' and i[int(s) - 1] != c:
            ans = -1
            break
        else:
            i[int(s) - 1] = c
    if i[0] == '0' and N != 1:
        ans = -1
    else:
        for j in range(N):
            if i[j] == '' and j != 0:
                i[j] = '0'
        if i[0] == '' and N != 1:
            i[0] = '1'
        elif i[0] == '' and N == 1:
            i[0] = '0'
    if ans != -1:
        ans = int(''.join(i))
    print(ans)


def __starting_point():
    main()


__starting_point()

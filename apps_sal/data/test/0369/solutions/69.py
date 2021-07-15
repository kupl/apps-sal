import sys

input = sys.stdin.readline


def main():
    N, M = [int(x) for x in input().split()]
    S = input().strip()

    if S.count("1" * M) > 0:
        print((-1))
        return

    ans = []
    r = N
    while r > 0:
        li = N - 1
        for diff in range(1, M + 1):
            if r - diff < 0:
                break
            if S[r - diff] == "0":
                li = r - diff
        ans.append(r - li)
        r = li
        if r == 0:
            break

    ans.reverse()
    print((*ans))



def __starting_point():
    main()

__starting_point()

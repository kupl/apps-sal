import sys
def input(): return sys.stdin.readline().rstrip()


def main():
    n = int(input())
    a = list(map(int, input().split()))
    cnt = [0] * (max(a) + 3)

    for i in a:
        cnt[i - 1] += 1
        cnt[i] += 1
        cnt[i + 1] += 1

    print(max(cnt))


def __starting_point():
    main()


__starting_point()

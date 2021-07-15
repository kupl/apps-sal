3

def solve(N, S):
    cnt = [0] * 26
    for c in S:
        cnt[ord(c) - ord('a')] += 1

    colors = len([c for c in cnt if c > 0])

    if colors == 1:
        return True

    return max(cnt) >= 2


def main():
    N = int(input())
    S = input()
    print('Yes' if solve(N, S) else 'No')


def __starting_point():
    main()

__starting_point()

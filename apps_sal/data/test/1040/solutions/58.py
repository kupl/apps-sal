def main():
    import sys
    input = sys.stdin.readline
    N = int(input())
    S = input().strip()
    lenS = len(S)
    i = 1
    while i < lenS - 1:
        if S[i] == 'f':
            i += 1
            continue
        if S[i] != 'o':
            i += 2
            continue
        if S[i - 1] == 'f' and S[i + 1] == 'x':
            lenS -= 3
            S = S[:i - 1] + S[i + 2:]
            i = max(1, i - 2)
        else:
            i += 2
    print(lenS)


def __starting_point():
    main()


__starting_point()

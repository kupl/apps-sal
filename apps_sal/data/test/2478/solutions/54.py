def main():
    import sys

    def input():
        return sys.stdin.readline().strip()
    N = int(input())
    S = input()
    right = 0
    left = 0
    for i in range(N):
        if S[i] == '(':
            right += 1
        elif right:
            right -= 1
        else:
            left += 1
    print(left * '(' + S + right * ')')


def __starting_point():
    main()


__starting_point()

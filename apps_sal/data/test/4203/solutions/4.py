import sys
input = sys.stdin.readline


def main():
    S = list(input().strip())
    if S[0] == 'A' and S[2:-1].count('C') == 1:
        cnt = 0
        for s in S:
            if s.islower():
                cnt += 1
        if cnt == len(S) - 2:
            print('AC')
        else:
            print('WA')
    else:
        print('WA')


def __starting_point():
    main()


__starting_point()

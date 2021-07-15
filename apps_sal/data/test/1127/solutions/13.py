import sys
input = sys.stdin.readline


def main():
    t = int(input())
    for _ in range(t):
        N = int(input())
        S = input().strip()

        if N % 2 == 1:
            ans = 2
            for i in range(0, N, 2):
                if int(S[i]) % 2 == 1:
                    ans = 1
            print(ans)
        else:
            ans = 1
            for i in range(1, N, 2):
                if int(S[i]) % 2 == 0:
                    ans = 2
            print(ans)


def __starting_point():
    main()



__starting_point()

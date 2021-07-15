import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    S = input().rstrip()
    n = len(S)

    if S[0] == "A":
        cnt = 0
        for i in range(2, n - 1):
            if S[i] == "C":
                cnt += 1
        if cnt == 1:
            for i in range(n):
                if S[i] == "A" or S[i] == "C":
                    continue
                else:
                    if S[i].isupper():
                        print("WA")
                        break
            else:
                print("AC")
        else:
            print("WA")
    else:
        print("WA")


def __starting_point():
    resolve()

__starting_point()

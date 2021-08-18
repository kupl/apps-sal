import sys
from collections import Counter


def main():
    N = int(sys.stdin.readline())
    S = sys.stdin.readline().rstrip()

    cnt_dic = Counter(S)
    ans = cnt_dic["R"] * cnt_dic["G"] * cnt_dic["B"]

    for i in range(N):
        for j in range(i + 1, N):
            k = 2 * j - i

            if (k < len(S)) and (S[i] != S[j]) and (S[j] != S[k]) and (S[k] != S[i]):
                ans -= 1

    print(ans)


def __starting_point():
    main()


__starting_point()

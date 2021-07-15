import sys
from collections import Counter

input = sys.stdin.readline


def main():
    S = input().rstrip()
    T = input().rstrip()

    c_S = Counter(S)
    c_T = Counter(T)
    count_S = list(c_S.values())
    count_T = list(c_T.values())
    count_S.sort()
    count_T.sort()
    is_same = True
    for s, t in zip(count_S, count_T):
        if s != t:
            is_same = False
            break

    ans = "Yes" if is_same else "No"
    print(ans)


def __starting_point():
    main()

__starting_point()

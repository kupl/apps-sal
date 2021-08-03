import sys
from collections import defaultdict

sys.setrecursionlimit(10 ** 6)
INF = float("inf")
MOD = 10 ** 9 + 7


def input():
    return sys.stdin.readline().strip()


def main():
    S = input()
    N = len(S)
    K = int(input())

    places = defaultdict(list)
    for i in range(N):
        places[S[i]].append(i)

    places = sorted(list(places.items()), key=lambda x: x[0])
    words = set()
    for k, v in places:
        for start in v:
            cnt = 0
            for end in range(start + 1, N + 1):
                words.add(S[start:end])
                cnt += 1

                if cnt == 5:
                    break

        if len(words) >= 5:
            break

    words = sorted(words)
    print((words[K - 1]))


def __starting_point():
    main()


__starting_point()

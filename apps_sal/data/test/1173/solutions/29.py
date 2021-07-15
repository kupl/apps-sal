#!/usr/bin/env python3
import sys

def solve(N: int, A: "List[List[int]]"):
    for i in range(N):
        A[i] = A[i][::-1]
    
    answer = 0
    totalGame = 0
    MAXGAME = (N*(N-1))//2
    match = set()

    while True:
        if totalGame == 0:
            for i in range(N):
                if not A[i]:
                    continue
                match_index = A[i][-1]-1

                if not A[match_index]:
                    continue

                if match_index in match or i in match:
                    continue

                if A[match_index][-1]-1 == i:
                    A[i].pop()
                    A[match_index].pop()
                    match.add(i)
                    match.add(match_index)
                    totalGame += 1
        else:
            if totalGame == MAXGAME:
                break

            check_needed = list(match)
            # 既にこのターンでマッチしたインデックスを保持
            match = set()

            for i in check_needed:
                if not A[i]:
                    continue
                match_index = A[i][-1]-1

                if not A[match_index]:
                    continue

                if match_index in match or i in match:
                    continue

                if A[match_index][-1]-1 == i:
                    A[i].pop()
                    A[match_index].pop()
                    match.add(i)
                    match.add(match_index)
                    totalGame += 1

        if len(match) == 0:
            print((-1))
            return

        answer += 1

    print(answer)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    A = [[int(next(tokens)) for _ in range(N - 1)] for _ in range(N)]  # type: "List[List[int]]"
    solve(N, A)

def __starting_point():
    main()

__starting_point()

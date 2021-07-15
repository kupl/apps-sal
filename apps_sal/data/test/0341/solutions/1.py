#!/usr/bin/env python3
def main():
    N, K = list(map(int, input().split()))
    R, S, P = list(map(int, input().split()))
    T = input()

    command = [''] * N
    ans = 0
    for i, t in enumerate(T):
        if t == 'r':
            point = P
            command_candidate = 'p'
        elif t == 's':
            point = R
            command_candidate = 'r'
        else:
            point = S
            command_candidate = 's'

        if i >= K and command[i - K] == command_candidate:
            point = 0
            command_candidate = ''
        ans += point
        command[i] = command_candidate
    print(ans)


def __starting_point():
    main()

__starting_point()

import os
import sys
from collections import Counter


def main():
    (N, K) = list(map(int, input().split()))
    (R, S, P) = list(map(int, input().split()))
    T = input()
    takahashi = ''
    for t in T:
        if t == 's':
            takahashi += 'r'
        elif t == 'p':
            takahashi += 's'
        else:
            takahashi += 'p'
    for i in range(K, N):
        if takahashi[i - K] == takahashi[i]:
            takahashi = takahashi[:i] + '_' + takahashi[i + 1:]
    ans = takahashi.count('r') * R + takahashi.count('s') * S + takahashi.count('p') * P
    print(ans)


def __starting_point():
    main()


__starting_point()

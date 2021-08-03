from collections import Counter
import sys
input = sys.stdin.readline


def solve():
    T = int(input())
    anss = []
    for _ in range(T):
        N = int(input())
        As = list(map(int, input().split()))

        if N % 2:
            anss.append('Second')
        else:
            cnt = Counter(As)
            for value in list(cnt.values()):
                if value % 2:
                    anss.append('First')
                    break
            else:
                anss.append('Second')

    print(('\n'.join(anss)))


solve()

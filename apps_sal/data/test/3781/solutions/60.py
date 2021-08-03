from collections import Counter


def solve():
    N = int(input())
    a = list(map(int, input().split()))

    if N % 2:
        return 'Second'
    c = Counter(a)
    for x, y in c.items():
        if y % 2:
            return 'First'
    return 'Second'


T = int(input())

while(T):
    print(solve())
    T -= 1

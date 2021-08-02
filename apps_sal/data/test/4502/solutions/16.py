from collections import deque
from typing import List


def main():
    n = int(input())
    v = input().split(" ")
    print((*pp(n, v)))


def pp(n: int, v: List[str]) -> List[str]:
    x = []
    y = deque([])

    if n % 2 == 0:
        for i in range(n):
            if i % 2 == 0:
                y.append(v[i])
            else:
                x.append(v[i])
    else:
        for i in range(n):
            if i % 2 == 0:
                x.append(v[i])
            else:
                y.append(v[i])

    ret = []
    for i in range(len(x)):
        ret.append(x.pop())

    for i in range(len(y)):
        ret.append(y.popleft())

    return ret


def __starting_point():
    main()


__starting_point()

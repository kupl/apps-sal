import math  # noqa: F401
from collections import deque  # noqa: F401
from typing import Deque, Dict, List, Optional, Tuple, Union  # noqa: F401


def main(N: int, D: List[List[int]]):
    consecutive = 0
    for a, b in D:
        if a == b:
            consecutive += 1
            if consecutive >= 3:
                print("Yes")
                return
        else:
            consecutive = 0
    print("No")


def __starting_point():
    N = int(input())
    D: List[List[int]] = []
    for _ in range(N):
        a, b = list(map(int, input().split()))
        D.append([a, b])
    main(N, D)

__starting_point()

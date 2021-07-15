import math  # noqa: F401
from collections import deque  # noqa: F401
from typing import Deque, Dict, List, Optional, Tuple, Union  # noqa: F401


def main(S: str):
    if S[-1] != "s":
        print((S + "s"))
    else:
        print((S + "es"))


def __starting_point():
    S = input()
    main(S)

__starting_point()

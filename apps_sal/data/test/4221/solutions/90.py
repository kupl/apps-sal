import math
from collections import deque
from typing import Deque, Dict, List, Optional, Tuple, Union


def main(S: str):
    if S[-1] != "s":
        print((S + "s"))
    else:
        print((S + "es"))


def __starting_point():
    S = input()
    main(S)


__starting_point()
